# DEPT®
## QA AUTOMATION EXERCISE 
The exercise consists of developing a script using one automation tool that follow one of the following paths using this app > https://csb-x6dpt1.netlify.app/

### Path 1:
```
1. Load browser 
2. Check for network request to https://api.spacexdata.com/v3/rockets and verify response contains information for 4 rockets, and the field first_flight is in all cases later than 2005
3. Search “crs” on the UI search box
4. Check that 3 pages are being founded
5. Go to page 2 and mark CRS-13 as a favorite
6. Go to the Favorite tab and check that CRS-13 is there. 
7. Refresh browser and check again for step 5.
```
### Path 2:
```
1. Load browser 
2. Check for network request to https://api.spacexdata.com/v3/rockets and verify response is an array of length==4 and the field first_flight is in all cases later than 2005
3. Search “crx” 
4. Check that no results text is being displayed
5. Click “X” button inside the search input 
6. Check that 12 pages are being displayed again
7. Refresh browser and check again for step 5.
```