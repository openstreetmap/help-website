+++
type = "question"
title = "How do users use Open Streetmap?"
description = '''I&#x27;m aiming to plot various parish assets (street lamps, bins, benches, etc), so that my colleagues on the Parish Council can know where these things are and so that we can manage them efficiently. I&#x27;m beginning to learn how to plot these Nodes, but haven&#x27;t found out how my colleagues can view them. ...'''
date = "2021-04-22T13:28:00Z"
lastmod = "2021-04-27T11:58:00Z"
weight = 79807
keywords = [ "amenity" ]
aliases = [ "/questions/79807" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do users use Open Streetmap?](/questions/79807/how-do-users-use-open-streetmap)

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
<span id="post-79807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm aiming to plot various parish assets (street lamps, bins, benches, etc), so that my colleagues on the Parish Council can know where these things are and so that we can manage them efficiently. I'm beginning to learn how to <strong>plot</strong> these Nodes, but haven't found out how my colleagues can <strong>view</strong> them. And can they select to view just "our" assets? By definition, the parish is a relatively small area. Nonetheless, there is quite a lot of detail on the map that they don't need. Thanks in advance. PS. I struggled to find an appropriate tag for the "required" box.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '21, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/07f927b6fd206ce75743388e38547960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Barrie1956&#39;s gravatar image" />
<p><span>Barrie1956</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Barrie1956 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79807" class="comments-container">
&#10;</div>
<div id="comment-tools-79807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79807-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="79828"></span>

<div id="answer-container-79828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79828-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most powerful tool to display custom data is <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">Overpass-QL</a>, especially the <a href="http://overpass-turbo.eu">overpass-turbo</a> web interface.</p>
<p>For example, this <a href="http://overpass-turbo.eu/s/16xs">query</a>. Notice how I used the assistant (in the comments), really easy. You could build a complex query, "unioning" all the desired features. Then, in export, you get a link to display resulting map, on your website for example. You can even customize the rendering with <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS">mapCSS</a>, for example some color for benches, some other for bins.</p>
<p>Additionally, you could use <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a>. It's a powerful web application to make maps. You can draw whatever you want, but, better in your case, you can display data directly from OSM, using overpass queries. You could create a layer for each type of feature you wish to display, with different styles, and instruct these layer to get the relevant data using overpass. You can get popups, to display the data of the pulled nodes. I would use a static layer to display the frontier of the parish, if you want it, because it is usually a big request. So, download as gpx the relation 1608954 and children once, and upload it in uMap. You can also draw some stuff directly in uMap, if you don't want to clutter the OSM database with it, or for privacy or copyright reasons.</p>
<p>There are a lot of possible approaches, professionals like to use QGis, a promising interface is <a href="https://www.lizmap.com/">LizMap</a>, but there are others. But it's usually more complicated.</p>
<p>Hope this helps. Please comment or send message if you need more specific help, I could guide you setting up uMap.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '21, 20:09</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-79828" class="comments-container">
<span id="79883"></span>
<div id="comment-79883" class="comment">
<div id="post-79883-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi H_mlet Thanks for your answer. The deeper I get into this process, the more I find that it exceeds my abilities. AND, for the relatively simple task that I have, it would be disproportionate to the effort required to make it happen, even with help from you guys. (This reflects badly more on me than you!!) I'm going to try to find a simpler solution. I already have one or two idea. Thanks again.</p>
</div>
<div id="comment-79883-info" class="comment-info">
<span class="comment-age">(27 Apr '21, 11:58)</span> <span class="comment-user userinfo">Barrie1956</span>
</div>
</div>
</div>
<div id="comment-tools-79828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79828-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79808"></span>

<div id="answer-container-79808" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't have a direct answer to your question but I'd like to point you to our wiki page <a href="https://wiki.openstreetmap.org/wiki/OpenStreetMap_for_Government">OpenStreetMap for Government</a>. It's probably only a small sample of public body uses of OSM but maybe it gives you some ideas and hints.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '21, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79808" class="comments-container">
<span id="79810"></span>
<div id="comment-79810" class="comment">
<div id="post-79810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow. Thanks for the link, TZorn, but that is HEAPS more complex than what I'm aiming for. Maybe Open Streetmap is not the best platform for me and my task? Anyone else?</p>
</div>
<div id="comment-79810-info" class="comment-info">
<span class="comment-age">(22 Apr '21, 14:58)</span> <span class="comment-user userinfo">Barrie1956</span>
</div>
</div>
<span id="79811"></span>
<div id="comment-79811" class="comment">
<div id="post-79811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's fairly straightforward to search for stuff based on certain criteria (<a href="https://overpass-turbo.eu/s/16u7">here</a> is a search for car parks with a certain operator in a certain area) but without an example of what you want to do people won't be able to give specific replies.</p>
</div>
<div id="comment-79811-info" class="comment-info">
<span class="comment-age">(22 Apr '21, 15:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79808-form-container" class="comment-form-container">
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

