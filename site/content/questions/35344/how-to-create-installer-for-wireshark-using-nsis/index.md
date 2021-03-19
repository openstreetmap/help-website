+++
type = "question"
title = "How to create installer for Wireshark using NSIS"
description = '''I am creating an installer using NSIS. I want to detect whether user has installed correct version of Wireshark in his/her system or not. e.g. version 1.10.8. If this version is installed, then installer should proceed otherwise it should abort. I have created a basic code as shown below but don&#x27;t k...'''
date = "2014-08-09T04:10:00Z"
lastmod = "2014-08-10T07:06:00Z"
weight = 35344
keywords = [ "nsis", "wireshark" ]
aliases = [ "/questions/35344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create installer for Wireshark using NSIS](/questions/35344/how-to-create-installer-for-wireshark-using-nsis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35344-score" class="post-score" title="current number of votes">0</div><span id="post-35344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am creating an installer using NSIS. I want to detect whether user has installed correct version of Wireshark in his/her system or not. e.g. version 1.10.8. If this version is installed, then installer should proceed otherwise it should abort. I have created a basic code as shown below but don't know about how to detect the correct version. Following is my code:</p><pre><code>page license
page directory
Page instfiles

section &quot;VersionConfirmation&quot;
    # read the value from the registry into the $0 register
    ReadRegStr $0 HKLM &quot;Software\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark&quot; &quot;DisplayName&quot;

    # print the results in a popup message box
    MessageBox MB_OK &quot;Current Version of Wireshark is : $0&quot;
sectionEnd</code></pre><p>I also want to copy one script file to location like "C:\Program Files\Wireshark\Plugins" as per Wireshark installed version. How can I accomplish this. Any help would be greatly appreciated. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nsis" rel="tag" title="see questions tagged &#39;nsis&#39;">nsis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '14, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/ed793f28ef57deccbd04e511b2d6b291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Awesome&#39;s gravatar image" /><p><span>Awesome</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Awesome has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '14, 04:10</strong> </span></p></div></div><div id="comments-container-35344" class="comments-container"></div><div id="comment-tools-35344" class="comment-tools"></div><div class="clear"></div><div id="comment-35344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35373"></span>

<div id="answer-container-35373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35373-score" class="post-score" title="current number of votes">0</div><span id="post-35373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please check the original NSIS script for Wireshark.</p><blockquote><p>source code --&gt; packaging\nsis\wireshark.nsi</p></blockquote><p>That file contains code to check the version of the installed package and also code to copy a certain file. You can use that as an example.</p><p>Furthermore, please read the NSIS docs.</p><blockquote><p><a href="http://nsis.sourceforge.net/Docs/">http://nsis.sourceforge.net/Docs/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '14, 07:07</strong> </span></p></div></div><div id="comments-container-35373" class="comments-container"></div><div id="comment-tools-35373" class="comment-tools"></div><div class="clear"></div><div id="comment-35373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

