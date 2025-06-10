+++
type = "question"
title = "socket bind failed after running renderd"
description = '''Hey, basically I was setting up an osm tileserver. Now I&#x27;m at one point where I can&#x27;t fix the problem by myself. So here&#x27;s my problem: When I run renderd -f -c /usr/local/etc/renderd.conf I get the following output: renderd[28482]: Rendering daemon started renderd[28482]: Initiating reqyest_queue in...'''
date = "2019-04-29T12:41:00Z"
lastmod = "2019-07-07T03:28:00Z"
weight = 68998
keywords = [ "mysql", "renderd", "tileserver" ]
aliases = [ "/questions/68998" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [socket bind failed after running renderd](/questions/68998/socket-bind-failed-after-running-renderd)

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
<span id="post-68998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68998-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>basically I was setting up an osm tileserver. Now I'm at one point where I can't fix the problem by myself. So here's my problem:</p>
<p>When I run <code>renderd -f -c /usr/local/etc/renderd.conf</code> I get the following output:</p>
<p><code>renderd[28482]: Rendering daemon started renderd[28482]: Initiating reqyest_queue iniparser: syntax error in /usr/local/etc/renderd.conf (7): -&gt; ;[renderd01] iniparser: syntax error in /usr/local/etc/renderd.conf (14): -&gt; ;[renderd02] iniparser: syntax error in /usr/local/etc/renderd.conf (33): -&gt; ;** config options used by mod_tile, but not renderd ** iniparser: syntax error in /usr/local/etc/renderd.conf (45): -&gt; ;[style2] iniparser: syntax error in /usr/local/etc/renderd.conf (52): -&gt; ;** config options used by mod_tile, but not renderd ** renderd[28482]: Parsing section renderd renderd[28482]: Parsing render section 0 renderd[28482]: Parsing section mapnik renderd[28482]: Parsing section default renderd[28482]: config renderd: unix socketname=/var/run/renderd/renderd.sock renderd[28482]: config renderd: num_threads=4 renderd[28482]: config renderd: num_slaves=0 renderd[28482]: config renderd: tile_dir=/var/lib/mod_tile renderd[28482]: config renderd: stats_file=/var/run/renderd/renderd.stats renderd[28482]: config mapnik: plugins_dir=/usr/lib/mapnik/input renderd[28482]: config mapnik: font_dir=/usr/share/fonts/truetype renderd[28482]: config mapnik: font_dir_recurse=1 renderd[28482]: config renderd(0): Active renderd[28482]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock renderd[28482]: config renderd(0): num_threads=4 renderd[28482]: config renderd(0): tile_dir=/var/lib/mod_tile renderd[28482]: config renderd(0): stats_file=/var/run/renderd/renderd.stats renderd[28482]: config map 0: name(default) file(/home/betrieb/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(tile.openstreetmap.org) renderd[28482]: Initialising unix server socket on /var/run/renderd/renderd.sock socket bind failed for: /var/run/renderd/renderd.sock</code></p>
<p>I also tried the answers from <a href="https://stackoverflow.com/questions/16851034/i-get-an-error-saying-socket-bind-failed-for-var-run-renderd-renderd-sock-if-i">that post from stackoverflow</a> but it didn't help. Anyone another idea that can make it work?</p>
<p>Best regards,</p>
<p>N3x</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '19, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '19, 12:59</strong> </span></p>
</div>
</div>
<div id="comments-container-68998" class="comments-container">
<span id="68999"></span>
<div id="comment-68999" class="comment">
<div id="post-68999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which Linux distribution are you running?</p>
</div>
<div id="comment-68999-info" class="comment-info">
<span class="comment-age">(29 Apr '19, 13:04)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="69000"></span>
<div id="comment-69000" class="comment">
<div id="post-69000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ubuntu 18.04 lts server</p>
</div>
<div id="comment-69000-info" class="comment-info">
<span class="comment-age">(29 Apr '19, 13:08)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
</div>
<div id="comment-tools-68998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68998-form-container" class="comment-form-container">
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

<span id="69010"></span>

<div id="answer-container-69010" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you have a /var/run/renderd directory? Otherwise :</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<pre><code>sudo mkdir /var/run/renderd</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '19, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-69010" class="comments-container">
<span id="69012"></span>
<div id="comment-69012" class="comment">
<div id="post-69012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already created that folder before running it</p>
</div>
<div id="comment-69012-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 07:08)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69017"></span>
<div id="comment-69017" class="comment">
<div id="post-69017-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are the access rights to that folder and as what user are you trying to create a socket in there?</p>
</div>
<div id="comment-69017-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 09:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69018"></span>
<div id="comment-69018" class="comment">
<div id="post-69018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Didn't thought about that. Created with root and not it belongs to the user I'm executing the command with. Getting this output now: <a href="https://pastebin.com/pBADCg0P">https://pastebin.com/pBADCg0P</a> And when I try to open it in my Brwoser I get another error which I can't seem to get right now</p>
</div>
<div id="comment-69018-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 10:54)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69019"></span>
<div id="comment-69019" class="comment">
<div id="post-69019-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"An error occurred while loading the map layer 'default': Could not create datasource for type: 'postgis' (no datasource plugin directories have been successfully registered)" suggests you haven't don't the postgis part of that postgres setup. Maybe have a read of <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> and see what you might be missing?</p>
</div>
<div id="comment-69019-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 10:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69020"></span>
<div id="comment-69020" class="comment not_top_scorer">
<div id="post-69020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Funny thing is that I'm builing it using these instrustions. Just tried to do the postgres steps again but it seems like I already did everything right. I can only try to set up a new Server.</p>
</div>
<div id="comment-69020-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 12:16)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69031"></span>
<div id="comment-69031" class="comment not_top_scorer">
<div id="post-69031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't have multiple versions of postgres by any chance do you? Perhaps one has postgis set up but one not.</p>
</div>
<div id="comment-69031-info" class="comment-info">
<span class="comment-age">(01 May '19, 11:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69043"></span>
<div id="comment-69043" class="comment not_top_scorer">
<div id="post-69043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't. I tried to reinstall psql and correctly choose the owners but it still won't work. Warnings + Errors: <a href="https://pastebin.com/VhcaXtPC">https://pastebin.com/VhcaXtPC</a> Got any other idea?</p>
</div>
<div id="comment-69043-info" class="comment-info">
<span class="comment-age">(02 May '19, 12:53)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69055"></span>
<div id="comment-69055" class="comment not_top_scorer">
<div id="post-69055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was checking that pastebin and went to the file written in the error. Here's what I got: <a href="https://pastebin.com/WwEYdyLn">https://pastebin.com/WwEYdyLn</a> Is there any problem with that line or the whole layer?</p>
</div>
<div id="comment-69055-info" class="comment-info">
<span class="comment-age">(03 May '19, 07:57)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69060"></span>
<div id="comment-69060" class="comment">
<div id="post-69060-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That still says "Could not create datasource for type: 'postgis' (no datasource plugin directories have been successfully registered)". You'll need to resolve that before you can proceed. You say "I already did everything right" yet your computer disagrees with you.</p>
<p>Arguing with inanimate objects is rarely productive; and unfortunately only you know what you have <em>actually</em> done to get to where you are. Trying everything again on a new server (a small virtual machine, perhaps) would be one way to investigate what went wrong.</p>
</div>
<div id="comment-69060-info" class="comment-info">
<span class="comment-age">(03 May '19, 11:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69120"></span>
<div id="comment-69120" class="comment not_top_scorer">
<div id="post-69120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well... I set up a new VM and tried it again. Checked every step and set everything right. Still won't work. 2 VMs, same instructions, same result. Both won't work like they should.</p>
</div>
<div id="comment-69120-info" class="comment-info">
<span class="comment-age">(08 May '19, 07:51)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
</div>
<div id="comment-tools-69010" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69010-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69282"></span>

<div id="answer-container-69282" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69282-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Problem fixed - no answers needed anymore</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '19, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-69282" class="comments-container">
<span id="69284"></span>
<div id="comment-69284" class="comment">
<div id="post-69284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So what was it in the end?</p>
</div>
<div id="comment-69284-info" class="comment-info">
<span class="comment-age">(23 May '19, 15:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69286"></span>
<div id="comment-69286" class="comment">
<div id="post-69286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"What are the access rights to that folder and as what user are you trying to create a socket in there?" that comment helped a lot. And the database error was because I had to change <code>plugins_dir=/usr/lib/mapnik/input</code> to <code>plugins_dir=/usr/lib/mapnik/3.0/input</code></p>
</div>
<div id="comment-69286-info" class="comment-info">
<span class="comment-age">(23 May '19, 15:34)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
<span id="69913"></span>
<div id="comment-69913" class="comment">
<div id="post-69913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain what you did to solve it? I'm having the same problem. My plugins_dir is ok, the access rights seems to be my problem.</p>
</div>
<div id="comment-69913-info" class="comment-info">
<span class="comment-age">(07 Jul '19, 03:28)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-69282" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69282-form-container" class="comment-form-container">
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

