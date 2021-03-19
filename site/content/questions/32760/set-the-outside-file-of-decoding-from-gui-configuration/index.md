+++
type = "question"
title = "Set the outside file of decoding from GUI configuration"
description = '''I wrote a plugin for my protocol whose decoding depends on a file passed to it from the outside. Can I get that file can be properly set by acting directly on the properties of the plugin from the GUI of Wireshark? Thank you in advance.'''
date = "2014-05-13T07:09:00Z"
lastmod = "2014-05-15T03:29:00Z"
weight = 32760
keywords = [ "development", "input", "gui", "plugin" ]
aliases = [ "/questions/32760" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Set the outside file of decoding from GUI configuration](/questions/32760/set-the-outside-file-of-decoding-from-gui-configuration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32760-score" class="post-score" title="current number of votes">0</div><span id="post-32760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a plugin for my protocol whose decoding depends on a file passed to it from the outside. Can I get that file can be properly set by acting directly on the properties of the plugin from the GUI of Wireshark?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-input" rel="tag" title="see questions tagged &#39;input&#39;">input</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/beba516396947952b1ec047a91607492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Junzo&#39;s gravatar image" /><p><span>Junzo</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Junzo has one accepted answer">100%</span></p></div></div><div id="comments-container-32760" class="comments-container"></div><div id="comment-tools-32760" class="comment-tools"></div><div class="clear"></div><div id="comment-32760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32807"></span>

<div id="answer-container-32807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32807-score" class="post-score" title="current number of votes">2</div><span id="post-32807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming here that you want to set the pathname of the file from the GUI.</p><p>If so, you want to register a "filename" preference, which is a string preference that also supports a "Browse" button, allowing the user to browse the file system through the GUI. See, for example, <code>epan/dissectors/packet-kerberos.c</code>, which registers a "filename" preference using <code>prefs_register_filename_preference()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-32807" class="comments-container"><span id="32814"></span><div id="comment-32814" class="comment"><div id="post-32814-score" class="comment-score"></div><div class="comment-text"><p>Two questions:</p><p>Is the correct call every time the function of reading the string from the preferences by entering the function call in "dissect_myProto" or is there a way to invoke it only when the preference is changed?</p><p>How do I delete the preference, and then deallocate the string corresponding to the fie, when I close my wireshark?</p></div><div id="comment-32814-info" class="comment-info"><span class="comment-age">(15 May '14, 03:29)</span> <span class="comment-user userinfo">Junzo</span></div></div></div><div id="comment-tools-32807" class="comment-tools"></div><div class="clear"></div><div id="comment-32807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32778"></span>

<div id="answer-container-32778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32778-score" class="post-score" title="current number of votes">0</div><span id="post-32778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TPNCP dissector does something similar. Use a text entry for your file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '14, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-32778" class="comments-container"></div><div id="comment-tools-32778" class="comment-tools"></div><div class="clear"></div><div id="comment-32778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

