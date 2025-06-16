+++
type = "question"
title = "Get adress from osm.pbf with lat / lon via osmconvert results in almost only lat / lon entries"
description = '''Hi,  I am testin to extract a .csv file from the germany-latest.osm.pbf including latitude, longitude, street, hausnumber, and city. But when I let the following command run, I get a csv file with mainly only latitude and longitude entries, all the other address information is missing: ./osmconvert ...'''
date = "2016-08-18T10:53:00Z"
lastmod = "2020-08-11T09:33:00Z"
weight = 51518
keywords = [ "osmconvert", "germany-latest" ]
aliases = [ "/questions/51518" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get adress from osm.pbf with lat / lon via osmconvert results in almost only lat / lon entries](/questions/51518/get-adress-from-osmpbf-with-lat-lon-via-osmconvert-results-in-almost-only-lat-lon-entries)

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
<span id="post-51518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am testin to extract a .csv file from the germany-latest.osm.pbf including latitude, longitude, street, hausnumber, and city.</p>
<p>But when I let the following command run, I get a csv file with mainly only latitude and longitude entries, all the other address information is missing: ./osmconvert germany-latest.osm.pbf --csv="<a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a> <a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a> addr:street addr:housenumber addr:city" -o=3.csv</p>
<p>What am I doing wrong?</p>
<p>Thank you for your help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-germany-latest" rel="tag" title="see questions tagged &#39;germany-latest&#39;">germany-latest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '16, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeaae6ed1cbb7581b9338affb59e4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephano007&#39;s gravatar image" />
<p><span>Stephano007</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephano007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51518" class="comments-container">
&#10;</div>
<div id="comment-tools-51518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51518-form-container" class="comment-form-container">
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

<span id="51519"></span>

<div id="answer-container-51519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51519-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmconvert doesn't do any filtering. So <code>--csv="</code><a href="https://help.openstreetmap.org/users/5110/latroc"><code>@lat</code></a><code> </code><a href="https://help.openstreetmap.org/users/1350/longestaugust"><code>@lon</code></a><code> addr:street addr:housenumber addr:city"</code> includes every object with a latitude and longitude, which is every node in the file, regardless of whether it has an address or not.</p>
<p>You can take a look at the companion tool <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>. It first requires using osmconvert to translate the .pbf into a format it understands, you will likely want the <code>--all-to-nodes</code> option when you do this step. Many addresses are associated with OpenStreetMap ways and relations, objects which do not directly store location information. The <code>--all-to-nodes</code> will extract a location for them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '16, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-51519" class="comments-container">
&#10;</div>
<div id="comment-tools-51519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51519-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76101"></span>

<div id="answer-container-76101" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76101-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey, I saw your Question and would like to ask you if you found a solution for your Problem. I am completely new here and Need a list with all adresses of Germany as you described in the title.</p>
<p>Thank you very much in Advance!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '20, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/2ccc8631e81a11c9269669588a99e6af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isabellauefler&#39;s gravatar image" />
<p><span>isabellauefler</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isabellauefler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76101" class="comments-container">
&#10;</div>
<div id="comment-tools-76101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76101-form-container" class="comment-form-container">
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

