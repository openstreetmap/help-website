+++
type = "question"
title = "[HELP] Please! I want to delete Wireshark but i have some problems!"
description = '''please help, im stuck on &quot;Remove the wrapper scripts from /usr/local/bin and &quot;Unload the org.wireshark.ChmodBPF.plist launched job. and &quot;Remove /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist&quot; Please help! I wanted to test wireshark, now i wanna uninstall!'''
date = "2017-06-17T12:13:00Z"
lastmod = "2017-06-19T19:02:00Z"
weight = 62079
keywords = [ "wireshark", "help", "uninstall" ]
aliases = [ "/questions/62079" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[HELP\] Please! I want to delete Wireshark but i have some problems!](/questions/62079/help-please-i-want-to-delete-wireshark-but-i-have-some-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62079-score" class="post-score" title="current number of votes">0</div><span id="post-62079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>please help, im stuck on "Remove the wrapper scripts from /usr/local/bin and "Unload the org.wireshark.ChmodBPF.plist launched job. and "Remove /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist" Please help! I wanted to test wireshark, now i wanna uninstall!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '17, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/9d3bbaecde4b7da8c3fd26d75393c1b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shr00msz&#39;s gravatar image" /><p><span>shr00msz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shr00msz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '17, 12:16</strong> </span></p></div></div><div id="comments-container-62079" class="comments-container"></div><div id="comment-tools-62079" class="comment-tools"></div><div class="clear"></div><div id="comment-62079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62085"></span>

<div id="answer-container-62085" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62085-score" class="post-score" title="current number of votes">1</div><span id="post-62085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Put the following text into a shell script and run that script:</p><pre><code>#! /bin/sh
sudo rm -f \
    /usr/local/bin/capinfos \
    /usr/local/bin/dftest \
    /usr/local/bin/dumpcap \
    /usr/local/bin/editcap \
    /usr/local/bin/mergecap \
    /usr/local/bin/randpkt \
    /usr/local/bin/rawshark \
    /usr/local/bin/text2pcap \
    /usr/local/bin/tshark \
    /usr/local/bin/wireshark
sudo rm -f /etc/paths.d/Wireshark
sudo rm -f /etc/manpaths.d/Wireshark
sudo pkgutil --forget org.wireshark.cli.pkg
sudo rm -rf /Library/StartupItems/ChmodBPF
sudo rm -rf &quot;/Library/Application Support/Wireshark&quot;
sudo launchctl unload /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
sudo rm -f /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
sudo pkgutil --forget org.wireshark.ChmodBPF.pkg
sudo rm -rf /Applications/Wireshark.app
sudo pkgutil --forget org.wireshark.Wireshark.pkg</code></pre><p>(Yes, this means you'll have to open Terminal.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '17, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '17, 13:24</strong> </span></p></div></div><div id="comments-container-62085" class="comments-container"><span id="62148"></span><div id="comment-62148" class="comment"><div id="post-62148-score" class="comment-score"></div><div class="comment-text"><p>I did it, I don't know what happened, but it might have deleted, thanks.</p></div><div id="comment-62148-info" class="comment-info"><span class="comment-age">(19 Jun '17, 19:02)</span> <span class="comment-user userinfo">shr00msz</span></div></div></div><div id="comment-tools-62085" class="comment-tools"></div><div class="clear"></div><div id="comment-62085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

