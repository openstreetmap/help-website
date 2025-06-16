+++
type = "question"
title = "JOSM: How do I select a way for editing that is part of multiple relations"
description = '''I&#x27;m working on large multipolygons in northern Thailand which is giving me fits. My previous questions relating to this topic have been about splitting them. But I&#x27;ve given up on that for now in favor of simply modifying them to better suit the actual terrain. Which brings me to my present question:...'''
date = "2015-01-11T08:00:00Z"
lastmod = "2015-01-13T00:29:00Z"
weight = 40203
keywords = [ "josm", "editing", "relations" ]
aliases = [ "/questions/40203" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: How do I select a way for editing that is part of multiple relations](/questions/40203/josm-how-do-i-select-a-way-for-editing-that-is-part-of-multiple-relations)

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
<span id="post-40203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40203-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on large multipolygons in northern Thailand which is giving me fits. My previous questions relating to this topic have been about splitting them. But I've given up on that for now in favor of simply modifying them to better suit the actual terrain. Which brings me to my present question: There is one way (id:<a href="https://www.openstreetmap.org/way/140856543">140856543</a>) which is a member of 7 multipolygons, 5 boundary relations and 2 wood multipolygons. If I want to modify only one of the wood multipolygons I change all the others with it, which is not what I want.</p>
<p>How do I select only the relation that I want to edit?</p>
<p>Added this screenshot of the way in question <img src="/upfiles/Relations_in_JOSM.JPG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '15, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 14:14</strong> </span></p>
</div>
</div>
<div id="comments-container-40203" class="comments-container">
<span id="40211"></span>
<div id="comment-40211" class="comment">
<div id="post-40211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is the disadvantage when mappers combine objects where they shouldn't.<br />
IMHO you should remove the boundary way from the wood polygons and either create one from the boundary separate way both wood MPs do share or one way per wood MP as scai explains</p>
</div>
<div id="comment-40211-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 11:56)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-40203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40203-form-container" class="comment-form-container">
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

<span id="40204"></span>

<div id="answer-container-40204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40204-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To change the geometry of a relation you have to change its members. Because you don't want to change the geometry of all relations you will have to create a new way. The steps are as follows:</p>
<ul>
<li>Remove way 140856543 from the wood relation you want to change. You might have to split it first if the first and last nodes don't match exactly the start and end point of your intended geometry changes.</li>
<li>Draw a new way representing the section of the geometry that differs from the existing relations.</li>
<li>Add the new way to the wood relation.</li>
<li>Make sure the wood relation is closed again. JOSM's relation editor has a nice sort function where you can check whether the relation is closed.</li>
<li>Check whether the other relations you touched are still correct.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '15, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 09:21</strong> </span></p>
</div>
</div>
<div id="comments-container-40204" class="comments-container">
<span id="40217"></span>
<div id="comment-40217" class="comment">
<div id="post-40217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>, I need to better understand what you're saying. Are you telling me I should edit the particular multipolygon I'm interested in, search for the way numbered 140856543, remove it or split it or recreate it in some way, and then reattach it somehow?</p>
<p>Perhaps way 140856543 is the entire wood multipolygon, all 152 nodes of it. If I split it, aren't I also affecting that way in the other six relations?</p>
</div>
<div id="comment-40217-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 14:31)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40219"></span>
<div id="comment-40219" class="comment">
<div id="post-40219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, don't reattach it, reattach a newly created way instead. Remove it from the wood multipolygon so that way 140856543 is only used by the other relations but not by the wood multipolygon any more. Then create a new way just for your wood multipolygon and add it to the wood relation. Or in other words: Separate the relations by making them consist of individual ways. Sharing the same ways leads to the same geometry, a different geometry is only possible by using individual ways.</p>
</div>
<div id="comment-40219-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 14:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40228"></span>
<div id="comment-40228" class="comment">
<div id="post-40228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Okay, got it. I understand now. It's still going to be quite a task and I might defer it until I have enough time to finish all I want to do. I will simplify those multipolygons as I go so the next person who comes along won't have to deal with the multiple use problem.</p>
<p>Thanks very much.</p>
</div>
<div id="comment-40228-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 00:38)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-40204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40204-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40209"></span>

<div id="answer-container-40209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40209-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've covered something similar to this as part of the <a href="https://wiki.openstreetmap.org/wiki/Ireland/Mapping_Townlands">Irish Townland mapping project</a>. This section of the tutorial video should show you what to do</p>
<p><a href="https://www.youtube.com/watch?v=WG6Po8SmweE&amp;feature=youtu.be&amp;t=16m55s">https://www.youtube.com/watch?v=WG6Po8SmweE&amp;feature=youtu.be&amp;t=16m55s</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '15, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 11:43</strong> </span></p>
</div>
</div>
<div id="comments-container-40209" class="comments-container">
<span id="40215"></span>
<div id="comment-40215" class="comment">
<div id="post-40215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5669/dacor">@DaCor</a>,</p>
<p>I can already do what you show in your otherwise helpful video. In your example, you have a single relation with no others "on top" of it. In my situation I have 7 relations using the same way. Short of deleting a multipolygon and starting from scratch, something I'm never going to do, how can I separate the wood polygon of interest from the others before modifying it?</p>
</div>
<div id="comment-40215-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 13:59)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40216"></span>
<div id="comment-40216" class="comment">
<div id="post-40216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can only separate them by removing ways and adding new ones, as shown in DaCor's video tutorial and described in my answer. These relations are only "bound" together because they share the same ways, to fix this you have to make them use individual ways instead.</p>
</div>
<div id="comment-40216-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 14:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40218"></span>

<div id="answer-container-40218" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40218-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if you are overly familiar with relations so if I am being overly basic in my instruction please excuse me but scai has outlined the actions required above in his post so I will just expand on his instruction. The instruction is applicable anytime you wish to remove or add something from a relation, regardless if there is 1 or 7 relations sharing the same way.</p>
<p>First thing to note, you don't work on just one relation when you are doing these steps until you get to point # 4 below. Your actions affect all relations that share the way you are working on. This is not a reason for you not to proceed, just something you need to be aware of.</p>
<p>I am also assuming your question relates to adding or removing ways to existing relations to allow you to add/remove bits to the forest.</p>
<ol>
<li>In my video, at 19:20 you will see I select a node and split the way and then select another node and split again. This is to allow me to select the section I want to remove and only that section. Do this with your relation when you have a beginning and end node for the bit you want to modify. This isolates the section you want to remove/extend/modify</li>
<li>Next, at one of the points at which you split your relation, you want to draw a new way which reflects where you want your relation to be. The way should start where you did one of your splits and end where you did your other split so that once you edit the relation members you will still have a closed loop</li>
<li>Now select the section you split earlier</li>
<li>In the relation window, select the relation for your wood/forest and select edit</li>
<li>In the window that opens up, the way you split earlier will be highlighted, click the trashcan to remove it from your wood/forest relation</li>
<li>Now, without closing the relation editor, in the background, click on the new way you drew, it will show up on the right hand side of the relations editor, click one of the pink/blue buttons to add it to your relation</li>
<li>Now click the A&gt;Z button. Does your relation show a loop? If yes, happy days, save your change and upload, if not let me know</li>
</ol>
<p>Note, the video will go through the adding/deleting bits out of the relation from 19:00 onwards just incase you need something else to reference against</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '15, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 14:34</strong> </span></p>
</div>
</div>
<div id="comments-container-40218" class="comments-container">
<span id="40229"></span>
<div id="comment-40229" class="comment">
<div id="post-40229-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5669/dacor">@DaCor</a>,</p>
<p>Thanks very much. It's complicated but at least I understand what needs to be done now. As malenki says above, "That is the disadvantage when mappers combine objects where they shouldn't." I second that comment entirely. National and province boundaries must be superimposed but using those same ways for wood multipolygons was a bad idea.</p>
<p>Thanks for your detailed instructions and for making such a comprehensive video.</p>
<p>Cheers, Dave</p>
</div>
<div id="comment-40229-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 00:44)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40263"></span>
<div id="comment-40263" class="comment">
<div id="post-40263-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is no problem with utilising the same ways for multiple relations, I often do it. It makes more sense to do it sometimes. Other time, not so much and those times I don't.</p>
<p>Its fine so long as you know what you are doing and it only takes a bit of concentrated learning to get up to speed</p>
</div>
<div id="comment-40263-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 19:31)</span> <span class="comment-user userinfo">DaCor</span>
</div>
</div>
<span id="40270"></span>
<div id="comment-40270" class="comment">
<div id="post-40270-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I agree,and I too have done that on occasion. Lakes or reservoirs in heavily forested regions are good examples. But here there are large natural=wood multipolygons on either side of the national boundary which is entirely inside the wooded area for many miles. A straight line would have achieved the same purpose. But then I would have been deprived of a good learning experience &lt;g&gt;</p>
<p>Thanks again...</p>
</div>
<div id="comment-40270-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 00:20)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40271"></span>
<div id="comment-40271" class="comment">
<div id="post-40271-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>lol, thats a good way to look at it I suppsoe</p>
</div>
<div id="comment-40271-info" class="comment-info">
<span class="comment-age">(13 Jan '15, 00:29)</span> <span class="comment-user userinfo">DaCor</span>
</div>
</div>
</div>
<div id="comment-tools-40218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40218-form-container" class="comment-form-container">
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

