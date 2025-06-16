+++
type = "question"
title = "Faking missing timestamps of saved Garmin gpx-track"
description = '''The OSM FAQ contains the following advice: &quot;If you can&#x27;t get your GPX with timestamps with no mean, then you can use this command to fake them: xmlstarlet ed -N x=http://www.topografix.com/GPX/1/0 -N y=http://www.topografix.com/GPX/1/1 &#92;  -s &#x27;//x:trkpt|//y:trkpt&#x27; -t elem -n time -v 1970-01-01T00:00:...'''
date = "2012-04-09T15:01:00Z"
lastmod = "2012-04-10T00:09:00Z"
weight = 11828
keywords = [ "xml", "osmbegin", "gpx" ]
aliases = [ "/questions/11828" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Faking missing timestamps of saved Garmin gpx-track](/questions/11828/faking-missing-timestamps-of-saved-garmin-gpx-track)

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
<span id="post-11828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/FAQ">OSM FAQ</a> contains the following advice:</p>
<p>"If you can't get your GPX with timestamps with no mean, then you can use this command to fake them:</p>
<pre><code>xmlstarlet ed -N x=http://www.topografix.com/GPX/1/0 -N y=http://www.topografix.com/GPX/1/1 \
    -s &#39;//x:trkpt|//y:trkpt&#39; -t elem -n time -v 1970-01-01T00:00:00Z track.gpx &gt; track-nulltime.gpx</code></pre>
<p>"</p>
<p>My question:</p>
<p>"Where do I enter this command?"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-osmbegin" rel="tag" title="see questions tagged &#39;osmbegin&#39;">osmbegin</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '12, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/5aef5ae1d4dac489fadc81e1e801ff84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J%C3%BCrgen%20Frielinghaus&#39;s gravatar image" />
<p><span>Jürgen Friel...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jürgen Frielinghaus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '12, 20:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-11828" class="comments-container">
&#10;</div>
<div id="comment-tools-11828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11828-form-container" class="comment-form-container">
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

<span id="11844"></span>

<div id="answer-container-11844" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A web search suggests that it's referring to <a href="http://xmlstar.sourceforge.net/">this</a>. You'd enter the command at the command line in whatever operating system that your computer uses, but you'd need to install it first. The <a href="http://xmlstar.sourceforge.net/docs.php">documentation</a> suggests that the command might actually be "xml" rather than "xmlstarlet" for the current version.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '12, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11844" class="comments-container">
&#10;</div>
<div id="comment-tools-11844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11844-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11854"></span>

<div id="answer-container-11854" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a command entered into a <a href="http://en.wikipedia.org/wiki/Command-line_interpreter">command line interpreter</a> - which is different depending on the Operating System type of your computer.</p>
<p>This FAQ section is probably written with the Linux OS in mind and is just a hint for more advanced users.</p>
<p>It is dependent on the xmlstarlet program being installed first - different procedures for different OS's.</p>
<p>If you're using Windows then running cmd.exe is possible to enable entering the commands, but the example in the FAQ may not work:</p>
<ul>
<li>you'll probably have to enter the full path (folder) to reference the xmlstarlet (or xml) program</li>
<li>you'll need to know how to navigate the folder system to reference your gpx files.</li>
</ul>
<p>I'll reword the FAQ.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '12, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11854" class="comments-container">
&#10;</div>
<div id="comment-tools-11854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11854-form-container" class="comment-form-container">
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

