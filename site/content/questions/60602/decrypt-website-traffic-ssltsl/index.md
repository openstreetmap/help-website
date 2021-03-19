+++
type = "question"
title = "Decrypt website traffic SSL/TSL"
description = '''Having an issue with decrypting traffic from a game, not trying to cheat, just trying to scrape the leaderboards off :) In Environmental Variables, I&#x27;ve set SSLKEYLOGFILE to a text file. The file filled with all sorts of stuff, CLIENT_RANDOM and RSA things. I&#x27;ve then gone through WS and set PRE MAST...'''
date = "2017-04-06T01:47:00Z"
lastmod = "2017-04-12T14:05:00Z"
weight = 60602
keywords = [ "ssl", "ssl_decrypt", "decrypt", "decryption" ]
aliases = [ "/questions/60602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt website traffic SSL/TSL](/questions/60602/decrypt-website-traffic-ssltsl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60602-score" class="post-score" title="current number of votes">0</div><span id="post-60602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Having an issue with decrypting traffic from a game, not trying to cheat, just trying to scrape the leaderboards off :)</p><p>In Environmental Variables, I've set SSLKEYLOGFILE to a text file. The file filled with all sorts of stuff, CLIENT_RANDOM and RSA things.</p><p>I've then gone through WS and set PRE MASTER SECRET LOG FILE to the above file.</p><p>I have then started capturing with the filter TCP == 443 and loaded the website. Loads of packets come in, the sources are 2/3 different IPs. However, the packets do not seem to decrypt and I'm still left with the garbage text.</p><p>I've set the log file for SSL also but that's empty apart from these few lines:</p><pre><code>Wireshark SSL debug log

Wireshark version: 2.0.4 (v2.0.4-0-gdd7746e from master-2.0)
GnuTLS version:    3.2.15
Libgcrypt version: 1.6.2</code></pre><p>Any ideas how I can read this SSL/TSL feed in plain text or what am I doing wrong?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '17, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/10c6535def69c4f7a9a29b2123f86b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="King0r&#39;s gravatar image" /><p><span>King0r</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="King0r has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '17, 01:49</strong> </span></p></div></div><div id="comments-container-60602" class="comments-container"><span id="60603"></span><div id="comment-60603" class="comment"><div id="post-60603-score" class="comment-score"></div><div class="comment-text"><p>Have you started the capture before connecting with the game? The full handshake must be available for decryption to work.</p></div><div id="comment-60603-info" class="comment-info"><span class="comment-age">(06 Apr '17, 02:18)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="60657"></span><div id="comment-60657" class="comment"><div id="post-60657-score" class="comment-score"></div><div class="comment-text"><p>Yup even logged out completely, logged into the website and then loading the game up.</p></div><div id="comment-60657-info" class="comment-info"><span class="comment-age">(07 Apr '17, 08:36)</span> <span class="comment-user userinfo">King0r</span></div></div><span id="60784"></span><div id="comment-60784" class="comment"><div id="post-60784-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to try a newer Wireshark version? If you are using Ubuntu, install <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">ppa:wireshark-dev/stable</a></p></div><div id="comment-60784-info" class="comment-info"><span class="comment-age">(12 Apr '17, 14:05)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-60602" class="comment-tools"></div><div class="clear"></div><div id="comment-60602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60736"></span>

<div id="answer-container-60736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60736-score" class="post-score" title="current number of votes">0</div><span id="post-60736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well I'm still learning so forgive if I'm off base. Under Edit --&gt; Preferences --&gt; Protocols --&gt;SSL, there are some setting to add a key file, pass phrase, and debug file for reassemble.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '17, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/6239389f5173985899f83c6ac4046ac4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psiclonius&#39;s gravatar image" /><p><span>psiclonius</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psiclonius has no accepted answers">0%</span></p></div></div><div id="comments-container-60736" class="comments-container"></div><div id="comment-tools-60736" class="comment-tools"></div><div class="clear"></div><div id="comment-60736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

