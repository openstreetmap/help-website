+++
type = "question"
title = "How to resolve conflicts to replace deleted elements"
description = '''Initial Goal: My initial goal was to download an area from OSM using JOSM, run the JOSM validator on the area, and fix all errors and warnings that it reported. I do not intend to upload back to OSM. Background: I downloaded an area from OSM using the slippy map and query wizard on JOSM and deleted ...'''
date = "2022-06-28T11:44:00Z"
lastmod = "2022-06-30T10:19:00Z"
weight = 84907
keywords = [ "josm" ]
aliases = [ "/questions/84907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to resolve conflicts to replace deleted elements](/questions/84907/how-to-resolve-conflicts-to-replace-deleted-elements)

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
<span id="post-84907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84907-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Initial Goal: My initial goal was to download an area from OSM using JOSM, run the JOSM validator on the area, and fix all errors and warnings that it reported. I do not intend to upload back to OSM.</p>
<p>Background: I downloaded an area from OSM using the slippy map and query wizard on JOSM and deleted all elements outside of that area. I accidentally deleted some elements inside of the area. I then ran the JOSM validator and fixed all errors and warnings.</p>
<p>Attempts: To fix my error, I downloaded the area from OSM again using the query wizard and JOSM reported conflicts with my version and the server version. I was trying to resolve these conflicts by setting the merged version to “not deleted,” however, the option to "Apply Resolution" was not available. <a href="https://imgur.com/R9rUptn">Apply Resolution image</a> When I tried to select “resolve to their versions,” I got this error message, “Merging deleted objects failed.” <a href="https://imgur.com/MaS4d0d">Resolve versions image</a> <a href="https://imgur.com/dxVp8v7">Merging failed image</a></p>
<p>Objective: I am trying to ensure that all elements outside of the area are still deleted, while the elements inside the area are all there.</p>
<p>Question: How can I fix my error by making the newly downloaded elements stay deleted and the rest remain in my final area with 0 conflicts? <a href="https://gis.stackexchange.com/q/434260/207664">Here is the original question I posted to gis.stackexchange</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '22, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/51c86de0c429fb2c12434eb046697359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acaroselli&#39;s gravatar image" />
<p><span>acaroselli</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acaroselli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '22, 16:03</strong> </span></p>
</div>
</div>
<div id="comments-container-84907" class="comments-container">
<span id="84911"></span>
<div id="comment-84911" class="comment">
<div id="post-84911-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Won't deleting elements outside the area you downloaded delete them in OSM when you upload your changes? I'm not sure you'd want that either? As such it might be better to start again and skip the deleting step.</p>
</div>
<div id="comment-84911-info" class="comment-info">
<span class="comment-age">(28 Jun '22, 13:30)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="84917"></span>
<div id="comment-84917" class="comment">
<div id="post-84917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/339/edloach">@EdLoach</a> JOSM has a "purge" function. But I haven't read through whether it may help here.</p>
</div>
<div id="comment-84917-info" class="comment-info">
<span class="comment-age">(29 Jun '22, 08:43)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-84907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84907-form-container" class="comment-form-container">
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

<span id="84910"></span>

<div id="answer-container-84910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84910-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>STOP!</strong></p>
<p>It seems you have a misunderstanding about what you are doing. If you upload the data and have actually done what you describe, you will be deleting the elements outside of the area from the OSM database.</p>
<p>A possible way to not loose your work would be to save it in OSC format then remove all deletions, download the data for the area in question and then apply the OSC file. You can do the same with a saved OSM (JOSM-variant) file too, but because it contains all data in the area that is going to be -very- painful.</p>
<p>The only problem is that I don't believe JOSM has a way to save changes in OSC format except if there is a plugin that will do that.</p>
<p>The not-particularly-direct method would be to save to OSM format, load that in Vespucci, save to OSC format and then return to JOSM.</p>
<p>PS: OSC files use the .osc file extension</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '22, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '22, 13:57</strong> </span></p>
</div>
</div>
<div id="comments-container-84910" class="comments-container">
<span id="84912"></span>
<div id="comment-84912" class="comment">
<div id="post-84912-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is OCS yet another OSM format or do you mean .osc ?</p>
</div>
<div id="comment-84912-info" class="comment-info">
<span class="comment-age">(28 Jun '22, 13:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84913"></span>
<div id="comment-84913" class="comment">
<div id="post-84913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Typo ... should be OSC</p>
</div>
<div id="comment-84913-info" class="comment-info">
<span class="comment-age">(28 Jun '22, 13:55)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="84914"></span>
<div id="comment-84914" class="comment">
<div id="post-84914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not intend to upload back to OSM.</p>
</div>
<div id="comment-84914-info" class="comment-info">
<span class="comment-age">(28 Jun '22, 16:06)</span> <span class="comment-user userinfo">acaroselli</span>
</div>
</div>
<span id="84915"></span>
<div id="comment-84915" class="comment">
<div id="post-84915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem is that both simply downloading fresh data or JOSMs update function will not override the deletions you made. So IMHO the way forward would still be saving to a file and manually editing it.</p>
</div>
<div id="comment-84915-info" class="comment-info">
<span class="comment-age">(28 Jun '22, 16:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="84921"></span>
<div id="comment-84921" class="comment">
<div id="post-84921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It may help that <a href="https://extract.bbbike.org/">https://extract.bbbike.org/</a> enables you to download osm in many formats within a self described polygon</p>
</div>
<div id="comment-84921-info" class="comment-info">
<span class="comment-age">(30 Jun '22, 10:19)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-84910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84910-form-container" class="comment-form-container">
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

