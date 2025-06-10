+++
type = "question"
title = "How do you download the change files?"
description = '''I must be missing something basic here. I am attempting to manually step through the process of getting change files from https://download.geofabrik.de/australia-oceania-updates/000/002/ so I can then automate via script. Curently my workflow is:   Initialise a working directory with config and down...'''
date = "2020-03-06T01:21:00Z"
lastmod = "2022-04-19T21:01:00Z"
weight = 73405
keywords = [ "changeset", ".osc", "osmosis", "replication" ]
aliases = [ "/questions/73405" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do you download the change files?](/questions/73405/how-do-you-download-the-change-files)

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
<span id="post-73405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73405-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I must be missing something basic here. I am attempting to manually step through the process of getting change files from <a href="https://download.geofabrik.de/australia-oceania-updates/000/002/">https://download.geofabrik.de/australia-oceania-updates/000/002/</a> so I can then automate via script.</p>
<p>Curently my workflow is:</p>
<ol>
<li><p>Initialise a working directory with config and download lock files with</p>
<p><strong>osmosis --read-replication-interval-init workingDirectory=%WORKOSM%</strong></p></li>
<li><p>Adjust the state date/time to something in the changelist then check the interval that should be covered by changes</p></li>
</ol>
<p><strong>osmosis -q --read-replication-lag humanReadable=yes workingDirectory=%WORKOSM%</strong></p>
<blockquote>
<p>11day(s) and 0 hour(s)</p>
</blockquote>
<ol>
<li>Then run an the command to download the change files</li>
</ol>
<p><strong>osmosis --rri workingDirectory=%WORKOSM% --wxc %WORKOSM%\change.osc.gz</strong></p>
<p>but all I get is a gzip of an empty xml file?? (1kB).</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osmChange version=&quot;0.6&quot; generator=&quot;Osmosis 0.47&quot;&gt;
&lt;/osmChange&gt;</code></pre>
<p>Can anyone help me with what I've done wrong here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '20, 01:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c3ff4a6fb6c4ca04f44e328fc275404c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quannah&#39;s gravatar image" />
<p><span>Quannah</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quannah has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '20, 01:26</strong> </span></p>
</div>
</div>
<div id="comments-container-73405" class="comments-container">
<span id="73406"></span>
<div id="comment-73406" class="comment">
<div id="post-73406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not a direct answer to the question, but from the perspective of keeping a tile server up to date you might find the notes <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a> useful. They use scripts such as <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/openstreetmap-tiles-update-expire">this one</a>. Rather than just downloading updates for one continent that script downloads everything but throws away what it doesn't want before loading the database. I'm sure that you can borrow from there to achieve what you want though.</p>
</div>
<div id="comment-73406-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 01:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73407"></span>
<div id="comment-73407" class="comment">
<div id="post-73407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! In the script (<a href="https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/openstreetmap-tiles-update-expire)">https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/openstreetmap-tiles-update-expire)</a> its line 155 that has me stumped. I just get an empty xml file. Should I be downloading all the .osc from the page and then merging them? The osmosis documentation makes it sound like that command should create an .osc file with all the changes inside.</p>
</div>
<div id="comment-73407-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 02:52)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
<span id="73413"></span>
<div id="comment-73413" class="comment">
<div id="post-73413-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I had written an answer but deleted that again because I think I was on the wrong track. Can you share the contents of the state.txt and configuration.txt files in your <code>%WORKOSM%</code> directory?</p>
</div>
<div id="comment-73413-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 08:21)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73486"></span>
<div id="comment-73486" class="comment">
<div id="post-73486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik - my state and config files look like:</p>
<p>--Thu Mar 05 15:17:54 AEST 2020 sequenceNumber=2543 timestamp=2020-03-04T21\:59\:03Z</p>
<p>and the configuration file looks like:</p>
<p>--The URL of the directory containing change files.</p>
<p>baseUrl=<a href="https://download.geofabrik.de/australia-oceania-updates/">https://download.geofabrik.de/australia-oceania-updates/</a></p>
<p>maxInterval = 604800</p>
</div>
<div id="comment-73486-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 01:48)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
</div>
<div id="comment-tools-73405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73405-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="73415"></span>

<div id="answer-container-73415" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73415-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please don't use Osmosis any more. Not only is it cumbersome to use, but Osmosis isn't maintained any more and contains known bugs.</p>
<p>Here is a better solution: <a href="https://github.com/osmcode/pyosmium/blob/master/doc/updating_osm_data.rst">https://github.com/osmcode/pyosmium/blob/master/doc/updating_osm_data.rst</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '20, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-73415" class="comments-container">
<span id="73487"></span>
<div id="comment-73487" class="comment">
<div id="post-73487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Jochen - but regardless of solution I think maybe I'm missing something basic in the state and config usage. I'll be sure to check out pyosmium - it looks easier to troubleshoot</p>
</div>
<div id="comment-73487-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 01:57)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
<span id="73489"></span>
<div id="comment-73489" class="comment">
<div id="post-73489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It does look good but I think having to build it from source is going to be an issue. I can work with python and shell commands but I'm not a C++ or .Net developer. Do you know if there is an installer or executable ?</p>
</div>
<div id="comment-73489-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 03:57)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
<span id="73490"></span>
<div id="comment-73490" class="comment">
<div id="post-73490-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are prebuild binaries available. You should be able to just "pip install osmium" as documented on <a href="https://github.com/osmcode/pyosmium">https://github.com/osmcode/pyosmium</a></p>
</div>
<div id="comment-73490-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 07:30)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-73415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77494"></span>

<div id="answer-container-77494" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77494-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A bit late but if you get the details of the state file of the day you downloaded your geofabrik file, then replace your current state file with the state of when you first downloaded. then you should see the change file populated. if should work with a state file from a couple days ago rather than when you first downloaded the geofabrik file but I haven't tested it. I think your osc file is empty because the state file might be the latest one, and osmosis will try to get the changes from that state file so the were wont be any chnages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '20, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77494" class="comments-container">
&#10;</div>
<div id="comment-tools-77494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77494-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84225"></span>

<div id="answer-container-84225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello all, To download change files from Geofabrik you can use my getdiff program from <a href="https://GitHub.com/waelhammoudeh/getdiff">https://GitHub.com/waelhammoudeh/getdiff</a> I hope this helps somebody</p>
<p>Good day</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '22, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/88d38e1916b4f2210db71007b0b36b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wael&#39;s gravatar image" />
<p><span>Wael</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wael has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84225" class="comments-container">
&#10;</div>
<div id="comment-tools-84225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84225-form-container" class="comment-form-container">
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

