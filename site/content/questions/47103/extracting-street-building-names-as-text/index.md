+++
type = "question"
title = "Extracting street / building names as text"
description = '''Hi, Im trying to find a way of highlighting a particular site using the manual selector bbox and then getting the text data of just either the road names or the building names within that boundary. I&#x27;m a complete novice so any help would be greatly appreciated . Jason'''
date = "2015-12-11T16:49:00Z"
lastmod = "2015-12-14T09:29:00Z"
weight = 47103
keywords = [ "street", "manual", "names", "bbox", "selector" ]
aliases = [ "/questions/47103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting street / building names as text](/questions/47103/extracting-street-building-names-as-text)

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
<span id="post-47103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47103-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Im trying to find a way of highlighting a particular site using the manual selector bbox and then getting the text data of just either the road names or the building names within that boundary. I'm a complete novice so any help would be greatly appreciated .</p>
<p>Jason</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-manual" rel="tag" title="see questions tagged &#39;manual&#39;">manual</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-selector" rel="tag" title="see questions tagged &#39;selector&#39;">selector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '15, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/7a36fa78ad75f76eb5dd169beef8b95f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jason%20HH&#39;s gravatar image" />
<p><span>Jason HH</span><br />
<span class="score" title="38 reputation points">38</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jason HH has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47103" class="comments-container">
&#10;</div>
<div id="comment-tools-47103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47103-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="47112"></span>

<div id="answer-container-47112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47112-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I didn't know a way to get this data straight away as a file with just the names. But then <a href="https://help.openstreetmap.org/users/8708/mmd"></a><a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a></a> corrected <a href="http://overpass-turbo.eu/s/de1">my example</a> on how to get all the named roads within a bounding box. If you run <a href="http://overpass-turbo.eu/s/de4">his variant</a>, you get a clean CSV file straight away. Only thing left to do is remove duplicates.</p>
<p>The query was generated with the wizard you see at the top of the screen. I only wrote: highway= <em>and name=</em> . For buildings, you would just need to change highway to building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '15, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '15, 21:13</strong> </span></p>
</div>
</div>
<div id="comments-container-47112" class="comments-container">
<span id="47113"></span>
<div id="comment-47113" class="comment">
<div id="post-47113-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>How about CSV output: <a href="http://overpass-turbo.eu/s/de4">http://overpass-turbo.eu/s/de4</a></p>
</div>
<div id="comment-47113-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 21:02)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47114"></span>
<div id="comment-47114" class="comment">
<div id="post-47114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a> ! Updated my answer to include your example.</p>
</div>
<div id="comment-47114-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 21:08)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="47115"></span>
<div id="comment-47115" class="comment">
<div id="post-47115-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just updated the example, we don't want to get any names of the ways' nodes.</p>
</div>
<div id="comment-47115-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 21:12)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47120"></span>
<div id="comment-47120" class="comment not_top_scorer">
<div id="post-47120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much for taking the time to answer that is such a great help, it really is fantastic. Just on the off chance that you've time to look is there also a way to run the same for the building names, and the borough / county names, or perhaps a way to do all three at that same time in one list.</p>
</div>
<div id="comment-47120-info" class="comment-info">
<span class="comment-age">(12 Dec '15, 15:47)</span> <span class="comment-user userinfo">Jason HH</span>
</div>
</div>
<span id="47130"></span>
<div id="comment-47130" class="comment not_top_scorer">
<div id="post-47130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And rob you of a nice learning opportunity? :)</p>
<p>To get named buildings is terribly easy. Look at the code, it won't bite. The part that says way["highway"]["name"] asks the system for everything that is a way and has both a name and a highway tag. For buildings, all you would need to do is replace highway with building. One other thing to do, would be to include an extra line which says relation instead of way. Why? In the Openstreetmap universe, a closed way (end point is the same as beginning point of the line) is a polygon. And most builings are 'normal' polygons. But if you want to exclude a bit within this polygon, mostly for inner courtyards, the data needs to explain that one line is the outside of the building, and the other the inside. Relations do just this.</p>
</div>
<div id="comment-47130-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 12:10)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="47131"></span>
<div id="comment-47131" class="comment">
<div id="post-47131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For neighborhoods and the like, there is a nice user interface around: <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> You can drill down to the region you need, then right click to get all its "children". Shapefile export includes a DBF file with names.</p>
</div>
<div id="comment-47131-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 12:14)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="47132"></span>
<div id="comment-47132" class="comment">
<div id="post-47132-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Something that might be of use too, is to look for streets within a neighborhood instead of within a bounding box. This query <a href="http://overpass-turbo.eu/s/df9">http://overpass-turbo.eu/s/df9</a> will return all the named roads that have at least one node within the village of Zwalm. But if you need to be sure of getting the correct result (i.e. looking for Rome, U.S.A instead of Rome, Italy), you can include some information to limit results. For example, looking up Zwalm in OSM <a href="https://www.openstreetmap.org/relation/416206">https://www.openstreetmap.org/relation/416206</a> I find that it is a level 8 administrative relation. So this query is more likely to turn up exactly what we need: <a href="http://overpass-turbo.eu/s/dfa">http://overpass-turbo.eu/s/dfa</a></p>
</div>
<div id="comment-47132-info" class="comment-info">
<span class="comment-age">(13 Dec '15, 12:32)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="47150"></span>
<div id="comment-47150" class="comment not_top_scorer">
<div id="post-47150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again for your help. Its certainly a steep learning curve!</p>
</div>
<div id="comment-47150-info" class="comment-info">
<span class="comment-age">(14 Dec '15, 09:29)</span> <span class="comment-user userinfo">Jason HH</span>
</div>
</div>
</div>
<div id="comment-tools-47112" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47112-form-container" class="comment-form-container">
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

