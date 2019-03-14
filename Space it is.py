{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "version": "0.3.2",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "metadata": {
        "id": "YfM_vXSrCKGc",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        },
        "outputId": "f055c547-7312-432d-976d-d47e7476027b"
      },
      "cell_type": "code",
      "source": [
        "#!/bin/python3\n",
        "\n",
        "import json\n",
        "import turtle\n",
        "import urllib.request\n",
        "import time\n",
        "\n",
        "url = 'http://api.open-notify.org/astros.json'\n",
        "response = urllib.request.urlopen(url)\n",
        "result = json.loads(response.read())\n",
        "print('People in space:',result['number'])\n",
        "\n",
        "people = result['people']\n",
        "#print(people)\n",
        "\n",
        "for astro in people:\n",
        "  print(astro['name'])\n",
        "\n",
        "url = 'http://api.open-notify.org/iss-now.json'\n",
        "response = urllib.request.urlopen(url)\n",
        "result = json.loads(response.read())\n",
        "location = result['iss_position']\n",
        "lati=location['latitude']\n",
        "longi=location['longitude']\n",
        "print('Latitude :',lati)\n",
        "print('Longitude :',longi)\n",
        "\n"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "People in space: 6\n",
            "Oleg Kononenko\n",
            "David Saint-Jacques\n",
            "Anne McClain\n",
            "Alexey Ovchinin\n",
            "Nick Hague\n",
            "Christina Koch\n",
            "Latitude : -2.6319\n",
            "Longitude : -174.7620\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "-02RByzFSRvZ",
        "colab_type": "text"
      },
      "cell_type": "markdown",
      "source": [
        ""
      ]
    }
  ]
}