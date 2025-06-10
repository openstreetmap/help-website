+++
type = "question"
title = "Convert track to road"
description = '''Hello, I have some tracks representing 100 km&#x27;s of roads that I want to enter in OSM (these roads are not yet in OSM). I have cleaned up these tracks, so all stops and other junk are deleted from the tracks. Now I upload these tracks to Potlatch 2, but some track points disappear. See question: http...'''
date = "2011-11-05T19:45:00Z"
lastmod = "2011-11-05T21:07:00Z"
weight = 8844
keywords = [ "track", "to", "road" ]
aliases = [ "/questions/8844" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert track to road](/questions/8844/convert-track-to-road)

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
<span id="post-8844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have some tracks representing 100 km's of roads that I want to enter in OSM (these roads are not yet in OSM). I have cleaned up these tracks, so all stops and other junk are deleted from the tracks.</p>
<p>Now I upload these tracks to Potlatch 2, but some track points disappear. See question: <a href="http://help.openstreetmap.org/questions/8795/broken-track">http://help.openstreetmap.org/questions/8795/broken-track</a> And the track that has missing trackpoints: <a href="http://www.openstreetmap.org/user/JavierP/traces/1132678">http://www.openstreetmap.org/user/JavierP/traces/1132678</a> OR <a href="http://www.openstreetmap.org/user/JavierP/traces/1132690">http://www.openstreetmap.org/user/JavierP/traces/1132690</a> (If you edit these tracks you will see the problem. Or download and upload the track and look if you have the same problem)</p>
<p>The other option is to import the track in JOSM and convert this to a road. Is this possible? I have tried to find a way to do this in JOSM but I cannot find how to do. Who can help? (And please give me an accurate description, because I have spend enough time to find a way to convert tracks to roads).</p>
<p>The best way for me should be that the upload of tracks in Potlatch2 works. This works more simple than JOSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '11, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7a18c056063a165f36376a9288221284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JavierP&#39;s gravatar image" />
<p><span>JavierP</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JavierP has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '11, 20:03</strong> </span></p>
</div>
</div>
<div id="comments-container-8844" class="comments-container">
&#10;</div>
<div id="comment-tools-8844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8844-form-container" class="comment-form-container">
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

<span id="8846"></span>

<div id="answer-container-8846" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8846-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is technically possible to convert your track record to a road in JOSM, it is however not the encouraged way. If you have already made substantial effort to improve the track this could be an exception so here is how you do it:</p>
<ol>
<li>Open track in JOSM</li>
<li>Download OSM data from the area around</li>
<li>Right click the gpx trace in the layers' list (top right corner by default) and choose "Transfer to data layer" (or something similar I am not using english translation)</li>
<li>Use "Simplify way" (Shift + Y)</li>
<li>Manually delete any duplicate recordings, make sure you connect the new road where it sould be connected (junctions) and resolve any collisions (river crossings =&gt; bridge) and tag the new road... This can be done in Potlatch</li>
<li>Upload the result</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '11, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '11, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-8846" class="comments-container">
&#10;</div>
<div id="comment-tools-8846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8845"></span>

<div id="answer-container-8845" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8845-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In JOSM you can convert GPS tracks directly to OSM data: right click on the track in the "Layers" display select "Convert to data layer".</p>
<p>I should point out that this should be used with caution, typical GPS tracks will have far to many nodes, so you should at least simplify the ways substantially before actually uploading your work.</p>
<p>Simon</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '11, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '11, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-8845" class="comments-container">
&#10;</div>
<div id="comment-tools-8845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8845-form-container" class="comment-form-container">
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

