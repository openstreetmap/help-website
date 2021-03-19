+++
type = "question"
title = "how to setup relative Paths (e.g. SSL keys) in config files (portable)"
description = '''Hi, i&#x27;d like to use the portable Wireshark and preconfigure it for my colleagues. We often need to decrypt traces with some pre-shared SSL Private keys. I would like to setup the Keys (IPs, Ports, Protocols, Path to Private keys) and then distribute the config, or pack the config back into a package...'''
date = "2016-05-18T02:29:00Z"
lastmod = "2016-05-18T07:33:00Z"
weight = 52710
keywords = [ "configuration", "config", "portable", "ssl_decrypt" ]
aliases = [ "/questions/52710" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to setup relative Paths (e.g. SSL keys) in config files (portable)](/questions/52710/how-to-setup-relative-paths-eg-ssl-keys-in-config-files-portable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52710-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i'd like to use the portable Wireshark and preconfigure it for my colleagues. We often need to decrypt traces with some pre-shared SSL Private keys.</p><p>I would like to setup the Keys (IPs, Ports, Protocols, Path to Private keys) and then distribute the config, or pack the config back into a package to redistritube the portable wireshark.</p><p>however, i cant seem to find a way to make the paths to the SSL keys relative. I googled and there seems to be questions like this but i did not find a helpful answer.</p><p>Is there an easy way to specifiy a relative path in the ssl_keys file? Where would the paths be relative to? To the ssl_key file (i.e. a subfulder with the keys would be in the Data\ folder)?</p><p>Thanks for any useful advice.</p></div><div id="question-tags" class="tags-container tags">configuration config portable ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/6a957b4a3140d9da1c17d8612db6d949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aslmx&#39;s gravatar image" /><p>aslmx<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aslmx has no accepted answers">0%</span></p></div></div><div id="comments-container-52710" class="comments-container"></div><div id="comment-tools-52710" class="comment-tools"></div><div class="clear"></div><div id="comment-52710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52728"></span>

<div id="answer-container-52728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52728-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The paths to the RSA private key is relative to the current working directory (whatever directory that you started Wireshark from, typically your home directory).</p><p>To make it truly portable, you could create a wrapper script that changes the working directory to an appropriate location (i.e. the location of your configuration). For Windows, you could for example use this (untested) <code>run-wireshark.cmd</code> file:</p><pre><code>@echo off
: Change directory to the location of this script
cd %~dp0
path\to\wireshark.exe %*</code></pre><p>The file location in <code>ssl_keys</code> should then be relative to this directory. Pcaps can be dropped on this batch file too. Alternatively you could use the old <code>keys_list</code> option as described at <a href="https://wiki.wireshark.org/SSL,">https://wiki.wireshark.org/SSL,</a> something like <code>wireshark -okeys_list:... %*</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-52728" class="comments-container"><span id="52753"></span><div id="comment-52753" class="comment"><div id="post-52753-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That helped me! The paths are relative to the path wireshark.exe gets called from or to the working directory you specify in a desktop shortcut.</p></div><div id="comment-52753-info" class="comment-info"><span class="comment-age">(18 May '16, 22:37)</span> aslmx</div></div></div><div id="comment-tools-52728" class="comment-tools"></div><div class="clear"></div><div id="comment-52728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

