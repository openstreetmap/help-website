+++
type = "question"
title = "[closed] Rendering highway lanes"
description = '''Why does not Mapnik render highway lanes? There is a great inconsistency about what highway=trunk means... sometimes it is used for single lane roads (mostly in United Kingdom) and sometimes it is used for say 2nd grade motorways (multiple lanes, continental western Europe for instance). If we rende...'''
date = "2014-03-12T21:32:00Z"
lastmod = "2018-01-10T20:30:00Z"
weight = 31511
keywords = [ "rendering", "lanes", "highway" ]
aliases = [ "/questions/31511" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Rendering highway lanes](/questions/31511/rendering-highway-lanes)

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
<span id="post-31511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31511-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-31511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why does not Mapnik render highway lanes? There is a great inconsistency about what <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtrunk">highway=trunk</a> means... sometimes it is used for single lane roads (mostly in United Kingdom) and sometimes it is used for say 2nd grade motorways (multiple lanes, continental western Europe for instance). If we rendered highway lanes, this inconsistency would disappear.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '14, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>14 Mar '14, 13:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-31511" class="comments-container">
&#10;</div>
<div id="comment-tools-31511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is a feature request phrased as a question, not a request for help" by Richard 14 Mar '14, 13:04

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31544"></span>

<div id="answer-container-31544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31544-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you should talk first with the UK community and check with them why "trunk" seems inconsistent. It is possible that locally someone made a mistake about the "trunk" class.</p>
<p>The "highway=trunk" is also used differently depending on the country. Here is a <a href="https://wiki.openstreetmap.org/wiki/Highway:International_equivalence">table showing the international equivalence</a> of the "highway" tags.</p>
<p>You can contact the UK community through <a href="https://lists.openstreetmap.org/listinfo/talk-gb">this dedicated mailing list</a> (needs subscription).<br />
</p>
<p>Here, in short, I can only provide some generality : the "highway" class reflects its importance in the road grid. Usually the amount of lanes is related to this importance (more traffic=more lanes). We can expect that the amount of lanes is greater in motorways than in residential streets. You might find some exceptions but then, it should be carefully verified and see if it is not simply a mapping mistake.<br />
The rendering styles currently use the "highway" class to set the colour and line width. It's not using the tag "lanes=<em>" or "width=</em>", excepted perhaps for the very high zoom levels where these attributs can really impact the resulting images.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '14, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-31544" class="comments-container">
<span id="61573"></span>
<div id="comment-61573" class="comment">
<div id="post-61573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Lanes=&lt;value&gt; should only effect the width of the road based on their default lane width. And if possible you can add width=&lt;value&gt; and width:lanes:[forward/backwards]=&lt;value&gt;(“|” divider if needed)&lt;value&gt; for overriding the lanes default width. The lanes or the better option of lanes in conjunction with the width, should be the only thing rendered. This would fix a lot of visual understanding of roads in open areas or visually and statistically knowing if you can use the roads in tight spaces.</p>
</div>
<div id="comment-61573-info" class="comment-info">
<span class="comment-age">(10 Jan '18, 20:30)</span> <span class="comment-user userinfo">Mxdanger</span>
</div>
</div>
</div>
<div id="comment-tools-31544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31544-form-container" class="comment-form-container">
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

