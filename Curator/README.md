# Discord Bot: Curator

This bot was created to streamline the sharing of content in a Discord server.

## Situational Considerations
The owner of the server is an artist and uses a channel to archive work-in-progress updates of things they are working on.\
This archive channel is named 'wips.'

Descriptions of WIPs are written as follows:
``````
```
PROJECT NAME:         [Project Name]
PROJECT POLYCOUNT:    [Polycount]
STATUS:               [Status of Project]
```
``````

The owner would like to see all of the most current WIPs in a designated channel.\
This channel is named 'wips-current.'

The owner would like to share some current WIPs with others, but not all of them.

Members are kept anonymous to each other. Therefore, members need their own seperate channels.\
These channels are kept in a category titled 'Exhibit.'

# Overview of Functionality
## Case 1: Uploading a Work in Progress
1. Message is sent in #wips. It is ignored if it does not match the normal description format.
2. If the description is valid, a button-prompt is sent by Curator asking if it should be shared to the channels in the 'Exhibit' category.
3. If 'Yes' is selected, the WIP will be formatted and sent to both #wips-current and all 'Exhibit' channels.
4. If 'No' is selected, the WIP will be formatted and sent only to #wips-current.
5. Curator will search all of the WIPs in #wips-current and the 'Exhibit' channels. If the WIP being shared has the same project name as an existing WIP, then it will be deleted.

## Case 2: Populating a New Channel
1. Functionality not yet implemented - Coming soon.
