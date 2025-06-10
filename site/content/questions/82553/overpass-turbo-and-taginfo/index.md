+++
type = "question"
title = "overpass turbo and taginfo"
description = '''Hi, in wiki, you have this : wiki where it says that natural=marsh is deprecated. In taginfo, you have this : taginfo One month ago, there were over 700 responses, I corrected them all to good tags (sometimes to a marsh, sometimes to a pond, sometimes a more appropriate tag). To find all the items, ...'''
date = "2021-11-13T22:24:00Z"
lastmod = "2021-11-14T00:07:00Z"
weight = 82553
keywords = [ "overpass-turbo", "taginfo", "marsh" ]
aliases = [ "/questions/82553" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass turbo and taginfo](/questions/82553/overpass-turbo-and-taginfo)

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
<span id="post-82553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>in wiki, you have this : <a href="https://wiki.openstreetmap.org/wiki/Tag:wetland%3Dmarsh">wiki</a> where it says that natural=marsh is deprecated.</p>
<p>In taginfo, you have this : <a href="https://taginfo.openstreetmap.org/tags/?key=natural&amp;value=marsh#overview">taginfo</a></p>
<p>One month ago, there were over 700 responses, I corrected them all to good tags (sometimes to a marsh, sometimes to a pond, sometimes a more appropriate tag).</p>
<p>To find all the items, I used overpass turbo :</p>
<pre><code>[out:json];
&#10;(
  node[natural=marsh]({{bbox}});
  way[natural=marsh]({{bbox}});
  relation[natural=marsh]({{bbox}});
);
&#10;out;
&gt;;
out skel qt;
</code></pre>
<p>I moved the map around the world to find all the objets and then used ID to correct them. After that, taginfo said that there was still one relation. I moved all over the world 3 more times, from the North Pole to the South Pole.</p>
<p>The last relation is invisible with overpass turbo.</p>
<p>Does anyone know how to find it ?</p>
<p>Best regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span> <span class="post-tag tag-link-marsh" rel="tag" title="see questions tagged &#39;marsh&#39;">marsh</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '21, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '21, 22:49</strong> </span></p>
</div>
</div>
<div id="comments-container-82553" class="comments-container">
&#10;</div>
<div id="comment-tools-82553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82553-form-container" class="comment-form-container">
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

<span id="82554"></span>

<div id="answer-container-82554" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82554-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(purely commenting on the overpass turbo side of things)</p>
<blockquote>
<p>The last relation is invisible with overpass turbo.</p>
</blockquote>
<p>If you click through from taginfo to Overpass turbo you get <a href="https://overpass-turbo.eu/s/1cZy">https://overpass-turbo.eu/s/1cZy</a> . When you run it, you can click "data" at the top right and click through to find the offending item: <a href="https://www.openstreetmap.org/relation/3517749">https://www.openstreetmap.org/relation/3517749</a> .</p>
<p>Although there's no geographic information with the OSM objects (two linked relations not linked to any non-relation objects), you can see from the <a href="https://www.openstreetmap.org/changeset/20608556">changeset</a> where the mapper was working at the time.</p>
<p>You won't be able to delete those two orphan relations with iD, but it would do no harm to do so, since they have never directly referred to geographical objects. If you were really keen you could perhaps ask the original mapper where they were trying to add a marsh (in Russian), but they last edited a year ago and this edit was 7 years ago, so I suspect that you might not get an answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '21, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '21, 22:44</strong> </span></p>
</div>
</div>
<div id="comments-container-82554" class="comments-container">
<span id="82556"></span>
<div id="comment-82556" class="comment">
<div id="post-82556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this answer ! You were very fast, my respect !</p>
<p>One last question : if I import the result in JOSM (I almost never use it), do you think it will be able to delete both relations ? Or to add the relation to a way that I will be able to delete in ID ?</p>
<p>Best regards</p>
</div>
<div id="comment-82556-info" class="comment-info">
<span class="comment-age">(13 Nov '21, 23:10)</span> <span class="comment-user userinfo">Fred73000</span>
</div>
</div>
<span id="82557"></span>
<div id="comment-82557" class="comment">
<div id="post-82557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've certainly used JOSM for that sort of thing in the past, so I'd imagine that it would work. Various other low-level edit options exist (see the wiki), and they would work too.</p>
</div>
<div id="comment-82557-info" class="comment-info">
<span class="comment-age">(13 Nov '21, 23:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82558"></span>
<div id="comment-82558" class="comment">
<div id="post-82558-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I DID IT !! With level0. I created a node in ID, then added this node to the 2 relations with level0, then in ID I was able to see the 2 relations and then to delete everything, the old relations and the temporary node. Thanks a lot for your help !!</p>
</div>
<div id="comment-82558-info" class="comment-info">
<span class="comment-age">(14 Nov '21, 00:07)</span> <span class="comment-user userinfo">Fred73000</span>
</div>
</div>
</div>
<div id="comment-tools-82554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82554-form-container" class="comment-form-container">
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

