+++
type = "question"
title = "osm2pgsql - planet killed"
description = '''Hello, I know this has been posted many times, but no answer posted has been able to fix my problem. I&#x27;m trying to import planet-latest.osm (planet Open Street Map) I tried using the following command: osm2pgsql -c -S /usr/share/osm2pgsql/default.style --slim -d osm --flat-nodes /var/tmp/flat-nodes....'''
date = "2015-04-24T13:41:00Z"
lastmod = "2015-04-26T10:16:00Z"
weight = 42572
keywords = [ "planet", "osm2pgsql", "killed" ]
aliases = [ "/questions/42572" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql - planet killed](/questions/42572/osm2pgsql-planet-killed)

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
<span id="post-42572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I know this has been posted many times, but no answer posted has been able to fix my problem.</p>
<p>I'm trying to import <strong><em>planet-latest.osm</em></strong> (planet Open Street Map)</p>
<p>I tried using the following command:</p>
<p><strong>osm2pgsql -c -S /usr/share/osm2pgsql/default.style --slim -d osm --flat-nodes /var/tmp/flat-nodes.bin --number-processes 8 -C 25000 planet-latest.osm</strong></p>
<p>At the begining, it failed because my node cache wasn't high enough. After I increased it, I've read it was getting killed because I needed 40G ram without --slim, so I used slim. Then I've read it was killed because I needed --flat-nodes with --slim, so I used --flat-nodes. I can't find what I am doing wrong. I'm sure it is obvious for some of you what I am doing wrong. If you can help me, I would realy appreciate it. Thanks!</p>
<p>PS: I'm running on Ubuntu VM using 32G Ram VM has approx 1000G space available using 8 process</p>
<p>I get the message: Reading in file: planet-latest.osm Processing: Node(2418060k 86.4k/s) Way(0k 0.00k/s) Relation(0 0.00/s)Killed</p>
<p>And then I get back into command line.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-killed" rel="tag" title="see questions tagged &#39;killed&#39;">killed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '15, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/cf421a2e4f4a3756c8442780cc925d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qalisto&#39;s gravatar image" />
<p><span>Qalisto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qalisto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42572" class="comments-container">
<span id="42573"></span>
<div id="comment-42573" class="comment">
<div id="post-42573-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Check <code>dmesg</code> for a message containing <em>Out of memory</em> and/or <em>oomkiller</em>. If this message appears then you will need to add more ram or more swap, the latter being significantly slower.</p>
</div>
<div id="comment-42573-info" class="comment-info">
<span class="comment-age">(24 Apr '15, 13:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42574"></span>
<div id="comment-42574" class="comment">
<div id="post-42574-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>... and (just in case you haven't already done this) I'd definitely run the process all the way through on a smaller extract first - and obviously if you don't have a need to render the whole planet, it makes sense to use a smaller extract anyway.</p>
</div>
<div id="comment-42574-info" class="comment-info">
<span class="comment-age">(24 Apr '15, 14:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42572-form-container" class="comment-form-container">
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

<span id="42602"></span>

<div id="answer-container-42602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42602-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As scai has pointed out you are likely running out of memory, you will need to add swap (which while slower is still preferrable to any other solution). Further I would suggest not running with 8 threads which, given the size of your machine, is likely to be counter productive.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '15, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42602" class="comments-container">
&#10;</div>
<div id="comment-tools-42602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42602-form-container" class="comment-form-container">
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

