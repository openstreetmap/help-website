+++
type = "question"
title = "How to change the default capture options for Linux based wireshark GUI"
description = '''I am trying to find a way to set the default capture options. I would like to have my capture by default stop capturing after 5MB. The default is curranly set to 1000KB. Is there a config file or enviroment variable that could be set to change the default capture options? This is for a Linux base bo...'''
date = "2012-09-25T12:35:00Z"
lastmod = "2012-09-25T17:59:00Z"
weight = 14516
keywords = [ "capture-defaults" ]
aliases = [ "/questions/14516" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to change the default capture options for Linux based wireshark GUI](/questions/14516/how-to-change-the-default-capture-options-for-linux-based-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14516-score" class="post-score" title="current number of votes">0</div><span id="post-14516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to find a way to set the default capture options. I would like to have my capture by default stop capturing after 5MB. The default is curranly set to 1000KB. Is there a config file or enviroment variable that could be set to change the default capture options? This is for a Linux base box and i'm needing these changes for the GUI.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-defaults" rel="tag" title="see questions tagged &#39;capture-defaults&#39;">capture-defaults</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '12, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/ee9a23ce91278d2d34048c29ee0fc84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tektron&#39;s gravatar image" /><p><span>Tektron</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tektron has no accepted answers">0%</span></p></div></div><div id="comments-container-14516" class="comments-container"></div><div id="comment-tools-14516" class="comment-tools"></div><div class="clear"></div><div id="comment-14516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14518"></span>

<div id="answer-container-14518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14518-score" class="post-score" title="current number of votes">0</div><span id="post-14518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the following, which will launch Wireshark and immediately begin capturing on interface <code>&lt;iface&gt;</code> while automatically stopping after 5MB of data has been captured.</p><pre><code>wireshark -i &lt;iface&gt; -k -a filesize:5000</code></pre><p>For more information on Wireshark's command-line options, refer to the <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a> or <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html">User Guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '12, 13:39</strong> </span></p></div></div><div id="comments-container-14518" class="comments-container"></div><div id="comment-tools-14518" class="comment-tools"></div><div class="clear"></div><div id="comment-14518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14520"></span>

<div id="answer-container-14520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14520-score" class="post-score" title="current number of votes">0</div><span id="post-14520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By default the preferences file for your user will be at:</p><p>~/.wireshark/preferences</p><p>While the system defaults are at:</p><p>/usr/share/wireshark/preferences</p><p>If you got Wireshark from your dirstobutions repositories (through yum or apt-get or somesuch) then your user preferences may be in root's home (/root/.wireshark/preferences). The global prefs file may also be elsewhere, "$which wireshark" will give you a clue.</p><p>The user prefs file will override (completely) the system prefs, same with the colorfilters files.</p><p>The wireshark docs have more info on what can be adjusted in the prefs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/7f557535084abef24cd30661f9daefad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CTNOBLE&#39;s gravatar image" /><p><span>CTNOBLE</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CTNOBLE has no accepted answers">0%</span></p></div></div><div id="comments-container-14520" class="comments-container"></div><div id="comment-tools-14520" class="comment-tools"></div><div class="clear"></div><div id="comment-14520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

