+++
type = "question"
title = "Windows 2.01 and Aruba GRE decode"
description = '''Hi! I can&#x27;t seem to get Windows Wireshark x64 2.01 to accomplish what this article suggests we do: http://community.arubanetworks.com/t5/Controller-Based-WLANs/How-can-we-see-the-packets-tunneled-inside-the-GRE-tunnel/ta-p/184910 They suggest a decodeas change to have Wireshark decode this GRE traff...'''
date = "2016-05-03T13:14:00Z"
lastmod = "2016-05-03T13:56:00Z"
weight = 52188
keywords = [ "decode_as", "aruba" ]
aliases = [ "/questions/52188" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 2.01 and Aruba GRE decode](/questions/52188/windows-201-and-aruba-gre-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52188-score" class="post-score" title="current number of votes">0</div><span id="post-52188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I can't seem to get Windows Wireshark x64 2.01 to accomplish what this article suggests we do:</p><p><a href="http://community.arubanetworks.com/t5/Controller-Based-WLANs/How-can-we-see-the-packets-tunneled-inside-the-GRE-tunnel/ta-p/184910">http://community.arubanetworks.com/t5/Controller-Based-WLANs/How-can-we-see-the-packets-tunneled-inside-the-GRE-tunnel/ta-p/184910</a></p><p>They suggest a decodeas change to have Wireshark decode this GRE traffic properly. I can't seem to configure this in the GUI, nor convince Wireshark to load a "decodeas" file..</p><p>Related to this, there has been some discussions about decoding Aruba-created GRE types.. how is that going in the 2.0 codebase?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span> <span class="post-tag tag-link-aruba" rel="tag" title="see questions tagged &#39;aruba&#39;">aruba</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/c1f107004c113d0a63ac8f06ad8d2a98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OldMonkey&#39;s gravatar image" /><p><span>OldMonkey</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OldMonkey has no accepted answers">0%</span></p></div></div><div id="comments-container-52188" class="comments-container"><span id="52196"></span><div id="comment-52196" class="comment"><div id="post-52196-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid it is not related to GRE directly but to the protocol ID indicated in the GRE header which you need to associate to the proper Ethertype dissector. Can you share (means: publish, login-free, somewhere like at Cloudshark, Dropbox, Google Drive, ..., and edit your Question with a link to it) a capture with at least a single packet like that so that we could have a look practically?</p></div><div id="comment-52196-info" class="comment-info"><span class="comment-age">(03 May '16, 13:56)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52188" class="comment-tools"></div><div class="clear"></div><div id="comment-52188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

