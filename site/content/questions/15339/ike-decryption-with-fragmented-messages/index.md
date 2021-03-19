+++
type = "question"
title = "IKE decryption with fragmented messages"
description = '''Hi, this Wireshark has a problem decrypting IKE messages when message 5 and 6 are fragmented and reassembled in Wireshark? I used the described method numerous times with OpenSwan and it worked like a charm. Then I changed to certificate based authentication and the payload exceeded the 1500 byte pa...'''
date = "2012-10-29T09:58:00Z"
lastmod = "2012-11-02T06:57:00Z"
weight = 15339
keywords = [ "fragment", "ike" ]
aliases = [ "/questions/15339" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IKE decryption with fragmented messages](/questions/15339/ike-decryption-with-fragmented-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15339-score" class="post-score" title="current number of votes">0</div><span id="post-15339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>this Wireshark has a problem decrypting IKE messages when message 5 and 6 are fragmented and reassembled in Wireshark? I used the described method numerous times with OpenSwan and it worked like a charm. Then I changed to certificate based authentication and the payload exceeded the 1500 byte packet size. Although I enter ICOOKIE and enc_key as the times before, I still see only encrypted data... I will enable JUMBO frames to verify this but maybe you have seen this before...</p><p>Cheers, Dominik</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-ike" rel="tag" title="see questions tagged &#39;ike&#39;">ike</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '12, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/9ef210346444f3db3b3a3bcfe88f0e63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dominik&#39;s gravatar image" /><p><span>Dominik</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dominik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>29 Oct '12, 13:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15339" class="comments-container"><span id="15344"></span><div id="comment-15344" class="comment"><div id="post-15344-score" class="comment-score"></div><div class="comment-text"><p>Converted from an "answer" to <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets</a></p></div><div id="comment-15344-info" class="comment-info"><span class="comment-age">(29 Oct '12, 13:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="15500"></span><div id="comment-15500" class="comment"><div id="post-15500-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>even with JUMBO frames it doesn't work. I have file a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7951">bug report</a> for this.</p><p>Cheers, Dominik</p></div><div id="comment-15500-info" class="comment-info"><span class="comment-age">(02 Nov '12, 06:57)</span> <span class="comment-user userinfo">Dominik</span></div></div></div><div id="comment-tools-15339" class="comment-tools"></div><div class="clear"></div><div id="comment-15339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

