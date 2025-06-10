+++
type = "question"
title = "Osmosis bat file runs then closes"
description = '''Similar to this question I am also having windows installation problems. I am using osmosis-0.39 and I have installed JRE, but when I run the batch file, it runs through some lines of code and then closes.  When I run the batch file in cmd, it looks like everything has run, &quot;org.openstreetmap.osmosi...'''
date = "2011-06-07T11:16:00Z"
lastmod = "2016-12-01T19:23:00Z"
weight = 5601
keywords = [ "osmosis" ]
aliases = [ "/questions/5601" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis bat file runs then closes](/questions/5601/osmosis-bat-file-runs-then-closes)

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
<span id="post-5601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5601-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Similar to <a href="http://help.openstreetmap.org/questions/1980/installing-osmosis">this question</a> I am also having windows installation problems. I am using osmosis-0.39 and I have installed JRE, but when I run the batch file, it runs through some lines of code and then closes.<br />
</p>
<p>When I run the batch file in cmd, it looks like everything has run, "org.openstreetmap.osmosis.core.Osmosis run, INFO: Total execution time: 562 milliseconds." but then what do I do?</p>
<p>This might be an absolutely obvious questions, but where am I actually writing the java commands into?</p>
<p>Sorry for such basic questions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '11, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/650c04578f8713eb2c8cf9dd3ab9b2f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nat%20Evatt&#39;s gravatar image" />
<p><span>Nat Evatt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nat Evatt has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>07 Jun '11, 18:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-5601" class="comments-container">
&#10;</div>
<div id="comment-tools-5601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5601-form-container" class="comment-form-container">
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

<span id="5617"></span>

<div id="answer-container-5617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5617-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think if you just run 'osmosis' while in the bin directory then it will start up (via the bat file), think about all the exciting tasks you given it (none whatsoever), and then report that it's finished. That's what you're seeing.</p>
<p>so try doing something like</p>
<pre><code>osmosis --read-xml C:\files\input.osm --write-xml C:\files\output.osm</code></pre>
<p>So now it's reading (trying to) and input file and writing an output file (.osm formatted XML) without doing anything in between (bit boring, but it should work)</p>
<p>Notice that I've specified paths in full. Kind of ugly perhaps. Another way of doing it would be to cd to the location where your planet files are and then specify the path to osmosis in full:</p>
<pre><code>cd c:\files
C:\Progra~1\osmosis\bin\osmosis --read-xml input.osm --write-xml output.osm</code></pre>
<p>Still pretty ugly perhaps, but you could put this in another bat file alongside your OSM files (a bat file calling a bat file) Command line params appearing after the word osmosis are fed through to the <a href="http://svn.openstreetmap.org/applications/utils/osmosis/trunk/package/bin/osmosis.bat">bat file in your osmosis installation</a> and I think little '%*' at the very end of that script, means your params (the specification of tasks etc) get fed into the osmosis java code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '11, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '11, 18:59</strong> </span></p>
</div>
</div>
<div id="comments-container-5617" class="comments-container">
<span id="5736"></span>
<div id="comment-5736" class="comment">
<div id="post-5736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Brilliant! Thank Harry.</p>
</div>
<div id="comment-5736-info" class="comment-info">
<span class="comment-age">(13 Jun '11, 17:59)</span> <span class="comment-user userinfo">Nat Evatt</span>
</div>
</div>
</div>
<div id="comment-tools-5617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5617-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53200"></span>

<div id="answer-container-53200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmosis is a bat file itself so call it with a CALL command to prevent closing after execution.</p>
<pre><code>CALL osmosis</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '16, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/6aec475eb732cafb533ee480a204ee7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yaugenka&#39;s gravatar image" />
<p><span>yaugenka</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yaugenka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53200" class="comments-container">
&#10;</div>
<div id="comment-tools-53200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53200-form-container" class="comment-form-container">
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

