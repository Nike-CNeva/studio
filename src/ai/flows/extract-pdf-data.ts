'use server';
/**
 * @fileOverview Extracts data such as number of sheets and waste from PDF files.
 *
 * - extractPdfData - A function that handles the PDF data extraction process.
 * - ExtractPdfDataInput - The input type for the extractPdfData function.
 * - ExtractPdfDataOutput - The return type for the extractPdfData function.
 */

import {ai} from '@/ai/ai-instance';
import {z} from 'genkit';
import {sendTelegramMessage} from '@/services/telegram';

const ExtractPdfDataInputSchema = z.object({
  pdfUrl: z.string().describe('The URL of the PDF file.'),
  chatId: z.string().optional().describe('The Telegram chat ID to send notifications to.'),
});
export type ExtractPdfDataInput = z.infer<typeof ExtractPdfDataInputSchema>;

const ExtractPdfDataOutputSchema = z.object({
  numberOfSheets: z.number().describe('The number of sheets extracted from the PDF.'),
  waste: z.string().describe('The waste information extracted from the PDF.'),
});
export type ExtractPdfDataOutput = z.infer<typeof ExtractPdfDataOutputSchema>;

export async function extractPdfData(input: ExtractPdfDataInput): Promise<ExtractPdfDataOutput> {
  return extractPdfDataFlow(input);
}

const extractPdfDataPrompt = ai.definePrompt({
  name: 'extractPdfDataPrompt',
  input: {
    schema: z.object({
      pdfUrl: z.string().describe('The URL of the PDF file.'),
    }),
  },
  output: {
    schema: z.object({
      numberOfSheets: z.number().describe('The number of sheets extracted from the PDF.'),
      waste: z.string().describe('The waste information extracted from the PDF.'),
    }),
  },
  prompt: `You are an expert in extracting data from PDF drawings for metal facade production.

You will analyze the PDF at the provided URL and extract the number of sheets and waste information.

PDF URL: {{pdfUrl}}

Extract the following information:
- Number of sheets: The total number of sheets required for the production.
- Waste: Any information about material waste, including quantity and type.

Ensure the extracted data is accurate and complete.`,
});

const extractPdfDataFlow = ai.defineFlow<
  typeof ExtractPdfDataInputSchema,
  typeof ExtractPdfDataOutputSchema
>({
  name: 'extractPdfDataFlow',
  inputSchema: ExtractPdfDataInputSchema,
  outputSchema: ExtractPdfDataOutputSchema,
  preprocessors: [async input => {
    if (input.chatId) {
      await sendTelegramMessage(input.chatId, 'Starting PDF data extraction...');
    }
    return input;
  }],
  postprocessors: [async (output, input) => {
    if (input.chatId) {
      await sendTelegramMessage(
        input.chatId,
        `PDF data extraction complete. Number of sheets: ${output.numberOfSheets}, Waste: ${output.waste}`
      );
    }
    return output;
  }],
},
async input => {
  const {output} = await extractPdfDataPrompt(input);
  return output!;
}
);

