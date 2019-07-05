#include <SFML/Graphics.hpp>

int main()
{
	sf::RenderWindow window( sf::VideoMode(800, 600), "SFML in VS Code!" );

	while(window.isOpen())
	{
		sf::Event windowEvent;
		while (window.pollEvent(windowEvent))
		{
			if (windowEvent.type == sf::Event::Closed)
				window.close();
		}

		window.clear( sf::Color::Red );

		window.display();
	}
}