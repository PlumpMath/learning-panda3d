#include "pandabase.h"
#include "pandaFramework.h"
#include "pandaSystem.h"

int main(int argc, char *argv[])
{
	//init framework
	PandaFramework framework;
	framework.open_framework(argc, argv);
	framework.set_window_title("Hello World!");

	//create a window
	WindowFramework *window = framework.open_window();

	//enable keyboard detection
	window->enable_keyboard();
	//enable default camera movement
	window->setup_trackball();

	//check if window opened successfully
	if (window != (WindowFramework *)NULL)
	{
		nout << "Opened window successfully!\n";

		//this is where loading of models and all that jazz would go

		framework.main_loop();
	}
	else
	{
		nout << "Failed to load window\n";
	}

	//clean up
	framework.close_framework();
	return 0;
}
