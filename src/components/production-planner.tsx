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

const taskSchema = z.object({
  title: z.string().min(2, {
    message: "Title must be at least 2 characters.",
  }),
  description: z.string().optional(),
});

type TaskValues = z.infer<typeof taskSchema>;

const TaskForm = () => {
  const form = useForm<TaskValues>({
    resolver: zodResolver(taskSchema),
    defaultValues: {
      title: "",
      description: "",
    },
  });

  function onSubmit(values: TaskValues) {
    console.log(values);
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
        <Button type="submit">Create Task</Button>
      </form>
    </Form>
  );
};

export const ProductionPlanner = () => {
  const router = useRouter();

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
            </CardContent>
          </Card>
        </div>
      </div>
    </>
  );
};
