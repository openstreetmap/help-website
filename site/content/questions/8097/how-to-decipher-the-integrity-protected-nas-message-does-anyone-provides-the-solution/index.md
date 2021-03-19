+++
type = "question"
title = "How to decipher  the integrity protected NAS message?? Does anyone provides the solution"
description = '''Hi All, In LTE network, NAS messages are intigrity protected. How to decipher them? Does wireshark has the solution for this? If no is there any solution or application for this in the market? Thanks in Advance Prithvi'''
date = "2011-12-22T20:49:00Z"
lastmod = "2017-05-31T03:17:00Z"
weight = 8097
keywords = [ "encrypted", "messages", "nas" ]
aliases = [ "/questions/8097" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decipher the integrity protected NAS message?? Does anyone provides the solution](/questions/8097/how-to-decipher-the-integrity-protected-nas-message-does-anyone-provides-the-solution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8097-score" class="post-score" title="current number of votes">0</div><span id="post-8097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>In LTE network, NAS messages are intigrity protected. How to decipher them? Does wireshark has the solution for this? If no is there any solution or application for this in the market?</p><p>Thanks in Advance</p><p>Prithvi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encrypted" rel="tag" title="see questions tagged &#39;encrypted&#39;">encrypted</span> <span class="post-tag tag-link-messages" rel="tag" title="see questions tagged &#39;messages&#39;">messages</span> <span class="post-tag tag-link-nas" rel="tag" title="see questions tagged &#39;nas&#39;">nas</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/f80796612a9bd2e5c17778ae0a41d8ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prithvi&#39;s gravatar image" /><p><span>prithvi</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prithvi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Dec '11, 20:49</strong> </span></p></div></div><div id="comments-container-8097" class="comments-container"><span id="8119"></span><div id="comment-8119" class="comment"><div id="post-8119-score" class="comment-score"></div><div class="comment-text"><p>The PDCP payload (RRC) that will carry NAS can be both ciphered (i.e. you can't read it without deciphering it) and integrity protected (i.e. there is a 4 byte MAC digest to prove that it is genuine). Do you mean this, or is there a separate mechanism for just the NAS messages?</p><p>I have looked at verifying that the integrity protection is correct. After sending ETSI an email asking if it was OK to implement this based upon their standard code (there is a large administration fee payable...), I got no reply.</p><p>In any case, getting all of the inputs right (for ciphering and/or integrity) would be hard to configure or work out correctly.</p></div><div id="comment-8119-info" class="comment-info"><span class="comment-age">(23 Dec '11, 15:43)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="8406"></span><div id="comment-8406" class="comment"><div id="post-8406-score" class="comment-score"></div><div class="comment-text"><p>I am asking about the encryption &amp; integrity at the node level. This will between eNodeB &amp; MME.</p></div><div id="comment-8406-info" class="comment-info"><span class="comment-age">(16 Jan '12, 03:40)</span> <span class="comment-user userinfo">prithvi</span></div></div><span id="8442"></span><div id="comment-8442" class="comment"><div id="post-8442-score" class="comment-score">1</div><div class="comment-text"><p>No one has implemented that functionality and I suspect that it is not easy to do so. You would also have to know the keys of both parties and have the initial exchange of keying material in the traces. I think the UEs key resides on the SIM so you would have to extract that some how.</p></div><div id="comment-8442-info" class="comment-info"><span class="comment-age">(17 Jan '12, 09:51)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="61706"></span><div id="comment-61706" class="comment"><div id="post-61706-score" class="comment-score"></div><div class="comment-text"><p>If we can capture S6a interface then using Authentication triplets try to match the S1 Call. Only for these matched calls we can get the keys from S6a interface &amp; do the decipher</p></div><div id="comment-61706-info" class="comment-info"><span class="comment-age">(31 May '17, 03:17)</span> <span class="comment-user userinfo">prithvi</span></div></div></div><div id="comment-tools-8097" class="comment-tools"></div><div class="clear"></div><div id="comment-8097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

