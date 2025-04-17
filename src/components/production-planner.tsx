"use client";

import {Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarInput, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarProvider, SidebarSeparator, SidebarTrigger} from "@/components/ui/sidebar";
import {Card, CardContent, CardDescription, CardHeader, CardTitle} from "@/components/ui/card";
import {Button} from "@/components/ui/button";
import {Icons} from "@/components/icons";
import {ScrollArea} from "@/components/ui/scroll-area";
import {Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger} from "@/components/ui/dialog";
import {Form, FormControl, FormDescription, FormField, FormItem, FormLabel} from "@/components/ui/form";
import {z} from "zod";
import {useForm} from "react-hook-form";
import {zodResolver} from "@hookform/resolvers/zod";
import {Input} from "@/components/ui/input";
import {Textarea} from "@/components/ui/textarea";
import {useRouter} from "next/navigation";
import {useEffect, useState} from "react";
import {createTask, readTasks} from "@/lib/api";
import {Select, SelectContent, SelectItem, SelectTrigger, SelectValue} from "@/components/ui/select";
import {getStatusOptions, getUrgencyOptions} from "@/lib/constants";

const taskSchema = z.object({
  title: z.string().min(2, {
    message: "Title must be at least 2 characters.",
  }),
  description: z.string().optional(),
  bid_id: z.number(),
  product_id: z.number(),
  material_id: z.number(),
  urgency: z.string(),
  status: z.string(),
});

type TaskValues = z.infer<typeof taskSchema>;

const TaskForm = () => {
  const form = useForm<TaskValues>({
    resolver: zodResolver(taskSchema),
    defaultValues: {
      title: "",
      description: "",
      bid_id: 1, // Default value
      product_id: 1, // Default value
      material_id: 1, // Default value
      urgency: 'LOW', // Default value
      status: 'NEW', // Default value
    },
  });

  async function onSubmit(values: TaskValues) {
    try {
      // Call the createTask function to submit data to the backend
      await createTask({
        bid_id: values.bid_id,
        product_id: values.product_id,
        material_id: values.material_id,
        urgency: values.urgency,
        status: values.status,
      });
      // Handle success (e.g., display a success message)
      console.log("Task created successfully!");
    } catch (error) {
      // Handle error (e.g., display an error message)
      console.error("Error creating task:", error);
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="title"
          render={({field}) => (
            <FormItem>
              <FormLabel>Title</FormLabel>
              <FormControl>
                <Input placeholder="Enter task title" {...field} />
              </FormControl>
              <FormDescription>
                This is the title of your task.
              </FormDescription>
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="description"
          render={({field}) => (
            <FormItem>
              <FormLabel>Description</FormLabel>
              <FormControl>
                <Textarea
                  placeholder="Enter task description"
                  className="resize-none"
                  {...field}
                />
              </FormControl>
              <FormDescription>
                Add a detailed description to your task.
              </FormDescription>
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="bid_id"
          render={({field}) => (
            <FormItem>
              <FormLabel>Bid ID</FormLabel>
              <FormControl>
                <Input type="number" placeholder="Enter Bid ID" {...field} />
              </FormControl>
              <FormDescription>
                Enter the Bid ID for this task.
              </FormDescription>
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="product_id"
          render={({field}) => (
            <FormItem>
              <FormLabel>Product ID</FormLabel>
              <FormControl>
                <Input type="number" placeholder="Enter Product ID" {...field} />
              </FormControl>
              <FormDescription>
                Enter the Product ID for this task.
              </FormDescription>
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="material_id"
          render={({field}) => (
            <FormItem>
              <FormLabel>Material ID</FormLabel>
              <FormControl>
                <Input type="number" placeholder="Enter Material ID" {...field} />
              </FormControl>
              <FormDescription>
                Enter the Material ID for this task.
              </FormDescription>
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="urgency"
          render={({field}) => (
            <FormItem>
              <FormLabel>Urgency</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select urgency"/>
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  {getUrgencyOptions().map((option) => (
                    <SelectItem key={option.value} value={option.value}>
                      {option.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <FormDescription>
                Select the urgency level for this task.
              </FormDescription>
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="status"
          render={({field}) => (
            <FormItem>
              <FormLabel>Status</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select status"/>
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  {getStatusOptions().map((option) => (
                    <SelectItem key={option.value} value={option.value}>
                      {option.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <FormDescription>
                Select the status for this task.
              </FormDescription>
            </FormItem>
          )}
        />

        <Button type="submit">Create Task</Button>
      </form>
    </Form>
  );
};

export const ProductionPlanner = () => {
  const router = useRouter();
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch tasks from the backend when the component mounts
    async function fetchTasks() {
      try {
        const tasksData = await readTasks();
        setTasks(tasksData);
      } catch (error) {
        console.error("Error fetching tasks:", error);
      }
    }

    fetchTasks();
  }, []);

  return (
    <>
      <Sidebar
        collapsible="icon"
        variant="inset"
      >
        <SidebarHeader className="h-14">
          <Icons.panelLeft className="mr-2 h-4 w-4"/>
          Production Planner
        </SidebarHeader>
        <SidebarInput placeholder="Search..."/>
        <SidebarSeparator/>
        <SidebarContent>
          <ScrollArea className="h-full">
            <SidebarMenu>
              <SidebarMenuItem>
                <SidebarMenuButton onClick={() => router.push('/')}>
                  <Icons.home className="mr-2 h-4 w-4"/>
                  <span>Home</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton onClick={() => router.push('/tasks')}>
                  <Icons.workflow className="mr-2 h-4 w-4"/>
                  <span>Tasks</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton onClick={() => router.push('/users')}>
                  <Icons.user className="mr-2 h-4 w-4"/>
                  <span>Users</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton onClick={() => router.push('/settings')}>
                  <Icons.settings className="mr-2 h-4 w-4"/>
                  <span>Settings</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </ScrollArea>
        </SidebarContent>
        <SidebarFooter>
          <p className="text-xs text-muted-foreground">
            Made by Firebase Studio
          </p>
        </SidebarFooter>
      </Sidebar>

      <div className="flex-1">
        <div className="border-b">
          <div className="flex h-16 items-center px-4">
            <SidebarTrigger className="mr-4 md:hidden"/>
            <div className="ml-auto flex items-center space-x-4">
              <Button size="sm" variant="ghost">
                <Icons.search className="mr-2 h-4 w-4"/>
                Search
              </Button>
              <Dialog>
                <DialogTrigger asChild>
                  <Button size="sm">
                    <Icons.plus className="mr-2 h-4 w-4"/>
                    Add Task
                  </Button>
                </DialogTrigger>
                <DialogContent className="sm:max-w-[425px]">
                  <DialogHeader>
                    <DialogTitle>Add Task</DialogTitle>
                    <DialogDescription>
                      Create a new task to manage production effectively.
                    </DialogDescription>
                  </DialogHeader>
                  <TaskForm/>
                </DialogContent>
              </Dialog>
            </div>
          </div>
        </div>
        <div className="p-4">
          <Card>
            <CardHeader>
              <CardTitle>Welcome to Production Planner</CardTitle>
              <CardDescription>
                This is a template for your production planning application.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p>Start building your application here.</p>
              <div>
                <h2>Tasks</h2>
                {tasks.length > 0 ? (
                  <ul>
                    {tasks.map((task) => (
                      <li key={task.id}>
                        Task ID: {task.id}, Urgency: {task.urgency}, Status: {task.status}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p>No tasks found.</p>
                )}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </>
  );
};
