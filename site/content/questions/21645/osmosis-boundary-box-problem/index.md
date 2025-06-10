+++
type = "question"
title = "Osmosis boundary box problem"
description = '''Hello, I am new to OSM and am trying to use Osmosis in Linux to extract an area of the UK to work with. I have used the command below as described on the web site but it comes back saying: Argument file for task 2-bounding-box was not recognised. My command is: osmosis --read-xml file=&quot;great-britain...'''
date = "2013-04-18T12:47:00Z"
lastmod = "2013-04-18T16:57:00Z"
weight = 21645
keywords = [ "osmosis" ]
aliases = [ "/questions/21645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis boundary box problem](/questions/21645/osmosis-boundary-box-problem)

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
<span id="post-21645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21645-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am new to OSM and am trying to use Osmosis in Linux to extract an area of the UK to work with. I have used the command below as described on the web site but it comes back saying:</p>
<p>Argument file for task 2-bounding-box was not recognised.</p>
<p>My command is: osmosis --read-xml file="great-britain-latest.osm" enableDateParsing=no file=- --bounding-box top=52 left=-7 bottom=39.5 right=-1 write-xml file="WestCountry.osm"</p>
<p>I'm not sure what the "file=-" just before --boundary-box is for but I tried taking that out and that didn't work either. Any help would be appreciated.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '13, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/88b618fb72eb0ea037e979ebe3ffc447?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christ0&#39;s gravatar image" />
<p><span>Christ0</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christ0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21645" class="comments-container">
&#10;</div>
<div id="comment-tools-21645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21645-form-container" class="comment-form-container">
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

<span id="21647"></span>

<div id="answer-container-21647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21647-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct invocation is (everything on one line of course):</p>
<pre><code>osmosis --read-xml file=&quot;great-britain-latest.osm&quot; enableDateParsing=no --bounding-box top=52 left=-7 bottom=39.5 right=-1 --write-xml file=&quot;WestCountry.osm&quot;</code></pre>
<p>(Note the double dash before write-xml.)</p>
<p>Both occurrences of <code>file=</code> are optional.</p>
<p>Your command line looks as if you downloaded and manually decompressed a Geofabrik extract. Your command will run much faster if you download the .pbf file and then instead of <code>--read-xml</code> use <code>--read-pbf</code> directly with the .pbf file you downloaded.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '13, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '13, 13:22</strong> </span></p>
</div>
</div>
<div id="comments-container-21647" class="comments-container">
<span id="21650"></span>
<div id="comment-21650" class="comment">
<div id="post-21650-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>also have a look at the programs called osmfilter and osmconvert ... search the OSM wiki about them.</p>
<p>In some scenarios they might be faster and easier to handle than osmosis.</p>
</div>
<div id="comment-21650-info" class="comment-info">
<span class="comment-age">(18 Apr '13, 16:46)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="21651"></span>
<div id="comment-21651" class="comment">
<div id="post-21651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help, I spotted the typo in the end and have managed to execute the command. I will try and use the other tools. It seems to take quite a long time to convert. I have a 10GB file of the UK and I am trying to extract the West Country. It has been sat there for four hours now saying:</p>
<p>Pipeline executing, waiting for completion.</p>
<p>The CPU is sat there at barely 5% useage and I can only assume that nothing is happening.</p>
<p>Is this correct?</p>
<p>Thanks</p>
</div>
<div id="comment-21651-info" class="comment-info">
<span class="comment-age">(18 Apr '13, 16:57)</span> <span class="comment-user userinfo">Christ0</span>
</div>
</div>
</div>
<div id="comment-tools-21647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21647-form-container" class="comment-form-container">
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

