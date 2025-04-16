"use client";

import {Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarInput, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarProvider, SidebarSeparator, SidebarTrigger} from "@/components/ui/sidebar";
import {Card, CardContent, CardDescription, CardHeader, CardTitle} from "@/components/ui/card";
import {Button} from "@/components/ui/button";
import {Icons} from "@/components/icons";
import {ScrollArea} from "@/components/ui/scroll-area";

export const ProductionPlanner = () => {
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
                <SidebarMenuButton>
                  <Icons.home className="mr-2 h-4 w-4"/>
                  <span>Home</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton>
                  <Icons.workflow className="mr-2 h-4 w-4"/>
                  <span>Tasks</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton>
                  <Icons.user className="mr-2 h-4 w-4"/>
                  <span>Users</span>
                </SidebarMenuButton>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <SidebarMenuButton>
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
              <Button size="sm">
                <Icons.plus className="mr-2 h-4 w-4"/>
                Add Task
              </Button>
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
