# Deictic relation task

## License

Copyright (c) Ian Hussey 2017 (ian.hussey@ugent.be)

Released under the GPLv3+ open source license. 

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
## Description
Implementation of the McHugh et al. perspective taking protocol.

*NB This code is still in beta - it hasn't been used it in a published article yet.*

- Inter trial interval is set to 1000 ms.

## Requirements
- [PsychoPy - v1.82](https://github.com/psychopy/psychopy/releases/tag/r1.82.02)
  - A free and open source program for delivering psychology experiments written in Python. See [here for documentation](http://www.psychopy.org/documentation.html).
  - PsychoPy runs locally on Windows, Mac, and Linux. It's not possible to run PsychoPy scripts online (yet).
  - You might be able to use more recent versions, but will probably need to run the `.py` file rather than the `.psyexp` file.


## Output
`.psydat`, `.csv` and `.log` files are produced for each participant. The `.csv` file alone is sufficient to most analyses. To my understanding, the format of the `.csv` output files are Tidy Data compliant (Wickham, 2014) and therefore easy to analyse (e.g., in R) with little to no processing needed.

## Issues 
If you have any issues, find bugs, or would like to see changes that you're not confident adding yourself please feel free to email me at [ian.hussey@ugent.be](mailto:ian.hussey@ugent.be). 

## To do 
1. Check task parameters with others with experience with the task (e.g., Louise McHugh, Roger Vilardega).
2. Swap out dummy stimuli for most up to date ones (check with Charlotte Dack).
3. Add an R processing script to do data processing.

## Changelog
### 0.1

- Initial upload