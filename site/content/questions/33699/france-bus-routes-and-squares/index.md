+++
type = "question"
title = "France bus routes and squares?"
description = '''Hi, Take a look at relation 1083434, it has a tag route_master = bus which means it refers to some bus routes and in this case:  Relation Bus 89 : Porte de France → Gare de Vanves-Malakoff (1246645) Relation Bus 89 : Gare de Vanves-Malakoff → Porte de France (1246644)  Which means there are directio...'''
date = "2014-06-05T08:57:00Z"
lastmod = "2014-06-12T13:43:00Z"
weight = 33699
keywords = [ "square", "busroute", "france" ]
aliases = [ "/questions/33699" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [France bus routes and squares?](/questions/33699/france-bus-routes-and-squares)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33699-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Take a look at <a href="https://www.openstreetmap.org/relation/1083434">relation 1083434</a>, it has a tag route_master = bus which means it refers to some bus routes and in this case:</p>
<ul>
<li>Relation Bus 89 : Porte de France → Gare de Vanves-Malakoff (1246645)</li>
<li>Relation Bus 89 : Gare de Vanves-Malakoff → Porte de France (1246644)</li>
</ul>
<p>Which means there are directional routes between two addresses.</p>
<p>Now that being said, if you look at <a href="https://www.openstreetmap.org/relation/1246644#map=17/48.82730/2.29332">Bus 89 : Gare de Vanves-Malakoff → Porte de France</a>, you will see a square (<a href="https://www.openstreetmap.org/way/23744258">Place d'Alleray</a>) that is included <strong>fully</strong> in the route! And same goes for the reverse direction of the other route!</p>
<p>Now my questions:</p>
<ul>
<li>Is this correct practice?</li>
<li>How do you actually calculate the bus route? It's not like the bus goes round and round before it continues the path, and we all know that squares are mostly uni-directional.</li>
<li>Is there a tag that I should be looking into that helps me resolve this?</li>
</ul>
<p>Any helps would be appreciated.</p>
<p>Thanks. :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-square" rel="tag" title="see questions tagged &#39;square&#39;">square</span> <span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '14, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9f6081b7d3a37174a676a7fce4d774c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aram%20Azhari&#39;s gravatar image" />
<p><span>Aram Azhari</span><br />
<span class="score" title="106 reputation points">106</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aram Azhari has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33699" class="comments-container">
<span id="33700"></span>
<div id="comment-33700" class="comment">
<div id="post-33700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I recently saw a comment to the effect that some software will process such relations correctly (probably on IRC). However, if the relation is used directly for visualising the route then, as here, it will look wrong.</p>
</div>
<div id="comment-33700-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 10:57)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33701"></span>
<div id="comment-33701" class="comment">
<div id="post-33701-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Visualization of the road itself is the less worrying factor for us. But let's say if you want to animate a bus moving on the route, then the case is that the bus has to follow a path and given that the square here is only one line, you cannot easily find where to exit. I mean I may be able to analyze the square and find out, but that is not preferred and only puts more weight on the system. So another question is, if this is a mistake, shall we fix it ?</p>
</div>
<div id="comment-33701-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 11:01)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33704"></span>
<div id="comment-33704" class="comment">
<div id="post-33704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@SK53</span> At least JOSM is able to handle such relations correctly, e.g. when ordering their elements. But I would expect difficulties in several end user applications.</p>
</div>
<div id="comment-33704-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 11:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33707"></span>
<div id="comment-33707" class="comment">
<div id="post-33707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@scai</span> What do you mean by handling? The order is not the issue here. If you read the post again, the issue is the incorrect inclusion of extra geometry.</p>
<p>In JOSM you can add as many lines as you like and call it a relation, but JOSM does not check if you have actually created an incorrect bus route.</p>
<p>It sometimes even gets worse. The person who draws the route tends to choose various line direction when drawing and as a result, current ending of a line may have a common node with the ending of the next line in the order!</p>
</div>
<div id="comment-33707-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 12:11)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33709"></span>
<div id="comment-33709" class="comment">
<div id="post-33709-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>JOSM actually allows you to check if the bus relation is correct. First you have the relation editor sort the route. Then there is the column with the arrows/lines and the roundabout symbol you can see in the picture in my answer below.</p>
</div>
<div id="comment-33709-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 12:27)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33699-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="33706"></span>

<div id="answer-container-33706" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33706-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some people will split roundabouts for routes, but many will not. There is even editor support in JOSM for having complete roundabouts in routes. See the roundabout symbol in the picture below. So please don't "fix" this.</p>
<p>There is no need for any special tagging for this.</p>
<p>JOSM is open source. So you can look at the code they used to check if the roundabout was connected properly: <a href="http://josm.openstreetmap.de/">http://josm.openstreetmap.de/</a></p>
<p><img src="/upfiles/RoundaboutRelation.png" alt="Roundabout in JOSM relation editor" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</img>
</div>
</div>
<div id="comments-container-33706" class="comments-container">
<span id="33716"></span>
<div id="comment-33716" class="comment not_top_scorer">
<div id="post-33716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does JOSM show you a uni directional arrow over the square? or does it draw the whole square circle and checks if they have connections with other parts of the route?</p>
<p>Assume that you come from line a to a square and then from square to line b (in order of appearance in relation). Which nodes of the square will the bus driver actually drive on? Is that somehow indicated in JOSM or OSM?</p>
</div>
<div id="comment-33716-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 14:28)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33721"></span>
<div id="comment-33721" class="comment">
<div id="post-33721-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to know what JOSM shows, then you should look at the picture above (at the end of the row highlighted in yellow).</p>
<p>If you want to visualize only part of the roundabout <em>you</em> have to calculate that. You know from which node the bus enters from the previous way. You know from which road it leaves from the next way. A junction=roundabout is oneway by definition, so there should only be one possibility.</p>
<p>OSM is a geodatabase with many data consumers but there are many more people adding data to it. When we "design" a tagging scheme, it should be easy to add the data foremost.</p>
</div>
<div id="comment-33721-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 15:14)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33724"></span>
<div id="comment-33724" class="comment not_top_scorer">
<div id="post-33724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that is what I had in mind when fixing. In the same route, some parts of the line are drawn in reverse and they are left for the application developers to guess the correct direction.</p>
<p>Assume that I am trying to create one line that merges all route lines. What happens is that some line that are in the order, are drawn the other way around (basically the data contributor had clicked to draw in the opposite direction). There I check if the end of the current line matches the start of the next line, if not I reverse the second line so it would match.</p>
<p>Now imagine this for our square...</p>
</div>
<div id="comment-33724-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 15:29)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33728"></span>
<div id="comment-33728" class="comment not_top_scorer">
<div id="post-33728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A line comes in order that enters, and then the square and after that, another line that also enters! Do you see my point?</p>
<p>If these errors happen together, it makes the data un-fixable and therefore should not be allowed. The easiest fix to this is to come up with a better standard. If it was an easy fix then the application developers would go ahead and do it, but if it requires multiple heuristic trials, then at least as a standard it should not be allowed.</p>
<p>Sure people can enter what they want in OSM, but there has to be a way to know what is right and what is not.</p>
</div>
<div id="comment-33728-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 15:34)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33729"></span>
<div id="comment-33729" class="comment">
<div id="post-33729-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You should only "fix" these things in you local copy. As these are <strong>not</strong> errors in the tagging.</p>
</div>
<div id="comment-33729-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 15:35)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33732"></span>
<div id="comment-33732" class="comment">
<div id="post-33732-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It should be noted that there is indeed an error with the relation. With a sole exception, the "forward" and "backward" roles have been neglected, leaving doubt as to which direction the route follows a way. Being a unidirectional route, every way member should have a role defining the direction. Adding these roles would eliminate the ambiguity mentioned by Aram about multiple ways pointing into a roundabout.</p>
</div>
<div id="comment-33732-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 17:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="33762"></span>
<div id="comment-33762" class="comment not_top_scorer">
<div id="post-33762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A square is uni-directional by implication. But there are ways in this route where the direction is not defined but the nodes are in the reverse order. So it has to be fixed (by application) to have the proper order. Same goes for the square. If the person starts drawing the nodes clockwise or drawing them counterclockwise then we see the problem.</p>
</div>
<div id="comment-33762-info" class="comment-info">
<span class="comment-age">(07 Jun '14, 07:51)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33763"></span>
<div id="comment-33763" class="comment not_top_scorer">
<div id="post-33763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, a square cannot necessarily have the start of its node on a line as there may be more than one entre/exit, but a bus route should absolutely be drawn regardless of the general shape of the street/square. Otherwise, I could just specify a bunch of lines selected from the actual roads and tell everyone one to guess the bus route.</p>
<p>I can draw a sketch to better visualize the problem.</p>
</div>
<div id="comment-33763-info" class="comment-info">
<span class="comment-age">(07 Jun '14, 07:51)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33773"></span>
<div id="comment-33773" class="comment not_top_scorer">
<div id="post-33773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't have to sketch anything as everybody understands you. If you have trouble understanding us, then maybe you can try <a href="https://lists.openstreetmap.org/listinfo/talk-fr">talk-fr@</a>, where you can ask questions and get answers in French (guessing that you are more fluent in that language).</p>
</div>
<div id="comment-33773-info" class="comment-info">
<span class="comment-age">(07 Jun '14, 10:16)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33822"></span>
<div id="comment-33822" class="comment not_top_scorer">
<div id="post-33822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately I don't speak French. I came to the realization that this discussion should be taken to the core team that define the standards, otherwise your statement does not overcome the presumption that 'the mentioned relations produce ambiguous and difficult-to-resolve bus routes and is merely a visual representation of the actual bus routes'</p>
</div>
<div id="comment-33822-info" class="comment-info">
<span class="comment-age">(09 Jun '14, 13:06)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33837"></span>
<div id="comment-33837" class="comment">
<div id="post-33837-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is no "core team that defines the standards" in OSM.</p>
</div>
<div id="comment-33837-info" class="comment-info">
<span class="comment-age">(09 Jun '14, 23:36)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="33840"></span>
<div id="comment-33840" class="comment not_top_scorer">
<div id="post-33840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then I guess given the fact that this is an openly collaborated database, I shall apply the corrections to the cloud and whoever that does not like it, may re-break it in their local copies.</p>
<p>Of course, at the end of the day we are all looking for a working headache free database that everyone can benefit.</p>
</div>
<div id="comment-33840-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 11:48)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
<span id="33841"></span>
<div id="comment-33841" class="comment">
<div id="post-33841-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As alester wrote above, one needs to add the forward/backward roles to each street segment in the relation that has to be followed in a particular direction. This is the direction you are looking for. This does not have to be added to the roundabout, as the direction for that is defined by the driving rules of the country.</p>
</div>
<div id="comment-33841-info" class="comment-info">
<span class="comment-age">(10 Jun '14, 12:53)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33917"></span>
<div id="comment-33917" class="comment not_top_scorer">
<div id="post-33917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can see that in <a href="https://www.openstreetmap.org/way/108025091">https://www.openstreetmap.org/way/108025091</a> (a part of this route) the person drew a circle and have mentioned in the note tag that "Ceci n'est pas un rond-point" or in other words, this is not a roundabout. What to do in this case?</p>
</div>
<div id="comment-33917-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 13:43)</span> <span class="comment-user userinfo">Aram Azhari</span>
</div>
</div>
</div>
<div id="comment-tools-33706" class="comment-tools">
<span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33706-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33705"></span>

<div id="answer-container-33705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In order to be usable by data consumers that don't have special handling to visualize the route, the roundabout Place d'Alleray would need to be split and the relations would need to be modified to include only the segment(s) actually crossed to get from an entrance to exit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-33705" class="comments-container">
<span id="33708"></span>
<div id="comment-33708" class="comment">
<div id="post-33708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When importing OSM data into a routing database ways have to be split at every junction. We don't split the ways at every junction in the OSM data either to make this easier for them. Similarly this is a "problem" that has to be fixed by the application and not by changing the data.</p>
</div>
<div id="comment-33708-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 12:21)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33904"></span>

<div id="answer-container-33904" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33904-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, After some research and with regards to those who commented on the issue, I am concluding and answering my own questions here:</p>
<ul>
<li>Is this correct practice? <strong>Answer</strong>: Just because JOSM does not throw any errors doesn't mean the route is correctly drawn, but there are many cases that more collaborators will simply select the square regardless of the fact that a bus route is different from s bus area. However, some suggest that the fixes should be applied to local copies and keep the main repository erroneous.</li>
<li>How do you actually calculate the bus route? It's not like the bus goes round and round before it continues the path, and we all know that squares are mostly uni-directional? <strong>Answer</strong>: First of all the direction of the lines must be specified to remove the confusion at the squares. Then by checking the intersection of the square with the entering/exiting lines find the right portion of the square that the bus should actually ride on.</li>
<li>Is there a tag that I should be looking into that helps me resolve this? <strong>Answer</strong>: Yes, the direction of the lines should help with the navigation, although in the mentioned relation example it is missing.</li>
</ul>
<p>Also, I realized that this was not the best route to give as an example. If you look at <a href="https://www.openstreetmap.org/relation/1246644#map=17/48.83273/2.37644">this</a> part of the route, you will clearly see that the person has made a mistake of drawing on the wrong side of the street and worse, create alternate dead-end paths.</p>
<p><strong>To resolve</strong> these up to some extent, you can iterate through the ways of the relation and if you want any way that does not have its both ends connected to some other ways, then remove it. Note that you should not touch the first and last way of the route as they are supposed to only be connected on one end. Also note that removing a dead end from the relation will only remove that tail of the dead-end path and may leave a new dead-ends and as a result you need to recursively do this on the updated list until you are left with no dead-end paths.</p>
<p>Best Regards,</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '14, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9f6081b7d3a37174a676a7fce4d774c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aram%20Azhari&#39;s gravatar image" />
<p><span>Aram Azhari</span><br />
<span class="score" title="106 reputation points">106</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aram Azhari has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '14, 10:11</strong> </span></p>
</div>
</div>
<div id="comments-container-33904" class="comments-container">
&#10;</div>
<div id="comment-tools-33904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33904-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

