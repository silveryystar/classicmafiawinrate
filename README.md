# Classic Mafia Winrate
A computational study of the relationship between winrate and player count in classic Mafia.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter `pip install matplotlib`.
5. Enter `pip install numpy`.
6. Enter `python main.py`.

# Abstract
In this study, village winrate in Mafia was analyzed under the lens of conservative, rational play by all players.
Under this lens, winrate was found to scale logarithmacally with integer village increases.
In particular, two distinct linear trends are established depending on whether an even or odd number of villagers are present in the game.

# Methodology
Mafia is a game classically played with a minimum of 6 players.
The game consists of two teams: the village and the mafia.
Together, these teams compose the town.

The village consists of two villagers, a cop, and a doctor.
The goal of the village is to eliminate all mafia.
The village accomplishes this by executing mafia during the day.
At night, the cop checks one town member, learning whether they are part of the village of the mafia.
At night, the doctor prevents one town member from dying.
The villagers do nothing at night.

On the other hand, the mafia consists of two mafia.
The mafia's goal is to eliminate as many village members as possible.
The mafia accomplishes this by murdering members of the village at night and executing village members during the day.
In particular, the mafia can kill one town member at night.
The village wins by eliminating all mafia, while the mafia wins by eliminating village members such that the number of mafia is greater than the number of villagers.

Two assumptions were made in this study: conservative and rational play.
Conservative play assumes protecting oneself above all.
Rational play assumes that all players act in a way that theoretically maximizes the chance of their team winning.

In particular, conservative play assumes:
1. The cop will not reveal themselves unless a mafia member is confirmed.
2. The doctor will self-heal.
3. The mafia will not counterclaim roles.

Rational play assumes:
1. The cop will not check the same player twice.
2. The cop will not check themselves.
3. The cop will not check a confirmed doctor.
4. The cop will not lead on an innocent player.
5. The doctor will heal a confirmed cop over oneself.
6. The mafia will not kill themselves.
7. The mafia will not target a confirmed cop while the doctor is alive.
8. The mafia will 50-50 if possible.
9. The town will follow cop leads.
10. If no cop leads occur, the town will execute no one on day 1, and random push unconfirmed players on day 2.

In practical games of mafia, rational play is often followed, while conservative play is not.
In particular, conservative play assumption 3 is often broken, as counterclaiming roles is a valid mafia strategy to deceive the village.
Conservative play assumption 2 is also occasionally broken, as the doctor attempts to outsmart the mafia and predict who will die.
Rational play assumptions 5 and 7 are also occasionally broken in practical play, as if the cop and the doctor are known, mafia and the doctor will often attempt to guess each other's action.

Despite these assumptions, the simulation roughly corresponds to real games.
In particular, a total of 11 million games were simulated for lineups ranging from 2 to 12 villagers.
The results of the simulation were then recorded to *results.txt* and plotted in log-log space, available as *Figure_0* in the repository.
*results.txt* also contains the linearized coefficients for the two lines in *Figure_0*.

# Results
This study concludes the following:
1. Assuming a conservative playstyle, village winrate is proportional to integer value villager increases.
2. In log-log space, this increase is linear.
3. Even villager counts (corresponding to an even total player count) corresponds to a greater village winrate than its n+1 (odd) counterpart.

Most people will likely find conclusion 1 obvious.
In most games, as you increase the number of players on a team, the chance of that team winning increases.
Likewise, to the mathematician, conclusion 2 is likely obvious.
In many games, winrate scales linearly in log-log space, as probability generally scales logarithmically when some advantage for one side is increased.

Conclusion 3 is new.
The winrate disparity between even and odd players is significant, and explains the changes in winrate between 2, 3, and 4 villagers in practical gameplay.
With a sample size of thousands of games, village winrate is ~51.5%, ~59.5%, and ~84.0% for 2, 3, and 4-villagers, respectively for human games.
Although this study finds a decrease in village winrate in the case of 3-players, it relatively predicts a large jump in winrate for 4 villagers, which is observed in real games.
Above all, this emphasizes the importance of using counterclaiming as mafia to cause confusion and role-calling as village to increase clarity.
A future simulation encompasses these gameplay plans would shed more light on the "perfect-play" winrates than this study offers. 

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
