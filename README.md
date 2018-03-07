#Footgoal
Predict football match winner. 
**More info -> check:  example.ipynb**

## Install:
```bash
pip install git+https://github.com/diwko/footgoal.git
```

## And run:
```bash
$ footgoal --home HOME_TEAM --away AWAY_TEAM
```

##Example:
```bash
$ footgoal --home Barcelona --away Chelsea

FIXTURES: FC Barcelona
2018-02-17                    SD Eibar    0 - 2    FC Barcelona             
2018-02-20                  Chelsea FC    1 - 1    FC Barcelona             
2018-02-24                FC Barcelona    6 - 1    Girona FC                
2018-03-01               UD Las Palmas    1 - 1    FC Barcelona             
2018-03-04                FC Barcelona    1 - 0    Club Atlético de Madrid  
(3, 2, 0, 8)


FIXTURES: Chelsea FC
2018-02-05                  Watford FC    4 - 1    Chelsea FC               
2018-02-12                  Chelsea FC    3 - 0    West Bromwich Albion FC  
2018-02-20                  Chelsea FC    1 - 1    FC Barcelona             
2018-02-25        Manchester United FC    2 - 1    Chelsea FC               
2018-03-04          Manchester City FC    1 - 0    Chelsea FC               
(1, 1, 3, -2)


HOME FIXTURES: FC Barcelona
2018-01-07                FC Barcelona    3 - 0    Levante UD               
2018-01-28                FC Barcelona    2 - 1    Deportivo Alavés         
2018-02-11                FC Barcelona    0 - 0    Getafe CF                
2018-02-24                FC Barcelona    6 - 1    Girona FC                
2018-03-04                FC Barcelona    1 - 0    Club Atlético de Madrid  
(4, 1, 0, 10)


AWAY FIXTURES: Chelsea FC
2018-01-03                  Arsenal FC    2 - 2    Chelsea FC               
2018-01-20      Brighton & Hove Albion    0 - 4    Chelsea FC               
2018-02-05                  Watford FC    4 - 1    Chelsea FC               
2018-02-25        Manchester United FC    2 - 1    Chelsea FC               
2018-03-04          Manchester City FC    1 - 0    Chelsea FC               
(1, 1, 3, -1)


H2H FIXTURES
2009-04-27                FC Barcelona    0 - 0    Chelsea FC               
2009-05-05                  Chelsea FC    1 - 1    FC Barcelona             
2012-04-17                  Chelsea FC    1 - 0    FC Barcelona             
2012-04-23                FC Barcelona    2 - 2    Chelsea FC               
2018-02-20                  Chelsea FC    1 - 1    FC Barcelona             
(0, 4, 1, -1) 

H2H FIXTURES H/A
2005-02-22                FC Barcelona    2 - 1    Chelsea FC               
2006-03-06                FC Barcelona    1 - 1    Chelsea FC               
2006-10-30                FC Barcelona    2 - 2    Chelsea FC               
2009-04-27                FC Barcelona    0 - 0    Chelsea FC               
2012-04-23                FC Barcelona    2 - 2    Chelsea FC               
(1, 4, 0, 1)


PREDICTED RESULT: FC Barcelona

```

## Treść zadania:

### Programowanie w jezyku Python 2016/2017 zadanie 2

Słowem roku 2016 w Oxford Dictionaries zostało wyrażenie post-truth (pl. “post-prawda”): https://en.oxforddictionaries.com/word-of-the-year/word-of-the-year-2016
Dotyczy ono pewnego sposobu kształtowania opinii publicznej w którym emocje i przekonania są ważniejsze niż fakty.

Przygotuj program służący do sprawdzania wiarygodności informacji. Program ten powinien analizować informacje dostępne w Internecie i wspomagać użytkownika w procesie weryfikacji prawdziwości znalezionej informacji.

Wymagania:
  - udostępnienie funkcjonalności programu w formie pakietu
  - wykorzystanie biblioteki numpy (lub innej opartej o nia) do manipulacji danymi
  - testy jednostkowe z wykorzystaniem biblioteki pytest albo nose
  - program powinien przejść test flake8 (zgodność z PEP8).

Pakiet ten powinien dać się wykorzystać w notatniku Jupyter. W ramach zadania proszę przygotować przykład użycia w notatniku Jupyter razem z opisem zastosowanego rozwiązania problemu i umieścić je w repozytorium.

Przydatna możw być następująca lista bibliotek: https://github.com/vinta/awesome-python

Dodatkowo trzeba wykonać trzy recenzje rozwiązań zadania nr 2 i umieścić w repozytorium w pliku review.txt odnośniki do odpowiednich “Pull request”. Ten fragment zadania umożliwia zdobycie maksymalnie 0.1 punktu.