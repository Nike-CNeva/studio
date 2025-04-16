import {SidebarProvider} from "@/components/ui/sidebar";
import {ProductionPlanner} from "@/components/production-planner";

export default function Home() {
  return (
    <SidebarProvider>
      <ProductionPlanner/>
    </SidebarProvider>
  );
}
