+++
type = "question"
title = "How is the FID generated for a SMB CreateAndx request?"
description = '''I see in the traces while accessing a network share, there are multiple CreateAndX requests(which opens the folders) with an FID associated with them. however, some of them dont and they get a different response.  292 7.561217000 client_Ip cifs_Server_ip SMB 184 NT Create AndX Request, FID: 0x1781, ...'''
date = "2015-03-22T22:49:00Z"
lastmod = "2015-03-24T22:46:00Z"
weight = 40773
keywords = [ "networking", "cifs", "share", "smb", "network" ]
aliases = [ "/questions/40773" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How is the FID generated for a SMB CreateAndx request?](/questions/40773/how-is-the-fid-generated-for-a-smb-createandx-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40773-score" class="post-score" title="current number of votes">0</div><span id="post-40773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see in the traces while accessing a network share, there are multiple CreateAndX requests(which opens the folders) with an FID associated with them. however, some of them dont and they get a different response.</p><p>292 7.561217000 client_Ip cifs_Server_ip SMB 184 NT Create AndX Request, FID: 0x1781, Path: \share_folder\subfolder</p><p>293 7.565304000 cifs_Server_ip client_Ip SMB 193 NT Create AndX Response, FID: 0x1781</p><p>320 7.761995000 clientIp cifs_Server_ip SMB 184 NT Create AndX Request, Path: \share_folder\subfolder</p><p>323 7.764860000 cifs_Server_ip client_ip SMB 93 NT Create AndX Response, FID: 0x0000, Error: STATUS_FILE_IS_A_DIRECTORY</p><p>The only differences between the two requests is that the first one doesnt have a FID and the CreateOptions field is set to 0x00000040(Non- directory field is set). The second request has this field set as 0. Both have access mask as 0x00120080.</p><p>The client is Windows7. Why are there two different consecutive CreateAndx requests and why are the getting a different response?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-cifs" rel="tag" title="see questions tagged &#39;cifs&#39;">cifs</span> <span class="post-tag tag-link-share" rel="tag" title="see questions tagged &#39;share&#39;">share</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '15, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/bc1e7422b9e06f3c3d9d6f68a870c202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerocool&#39;s gravatar image" /><p><span>xerocool</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerocool has no accepted answers">0%</span></p></div></div><div id="comments-container-40773" class="comments-container"></div><div id="comment-tools-40773" class="comment-tools"></div><div class="clear"></div><div id="comment-40773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40818"></span>

<div id="answer-container-40818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40818-score" class="post-score" title="current number of votes">0</div><span id="post-40818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In SMB the FID is send back to the client in the response. Wireshark will show the FID also on the request as it has learned the FID in the response. You can see that the FID is not in the packet, but supplied by wireshark by the square brackets around the FID.</p><p>So in frame 292, the FID is known, as it is supplied by the server in frame 293. But for the request in frame 320, there is no valid FID as there is an error and the response does not have a valid FID (FID=0x0000).</p><p>In short, no request has a FID, wireshark can add an FID to the request when the response has (a valid) one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40818" class="comments-container"><span id="40822"></span><div id="comment-40822" class="comment"><div id="post-40822-score" class="comment-score"></div><div class="comment-text"><p>Actually, FID = 0x0000 is valid according the [MS-CIFS] doc.</p><p>"The value 0xFFFF MUST NOT be used as a valid FID. All other possible values for FID, including zero (0x0000) are valid. The value 0xFFFF is used to specify all FIDs or no FID, depending upon the context in which it is used."</p><p>Also, how does Wireshark show the FID in request when its being obtained in the response? I mean its a little counter-intuitive</p></div><div id="comment-40822-info" class="comment-info"><span class="comment-age">(24 Mar '15, 19:54)</span> <span class="comment-user userinfo">xerocool</span></div></div><span id="40824"></span><div id="comment-40824" class="comment"><div id="post-40824-score" class="comment-score"></div><div class="comment-text"><p>During the first pass through the capture, Wireshark associates requests and responses for many protocols, including SMB. On that pass, it can't associate the FID with the request, as it hasn't seen the response yet.</p><p>On all subsequent references to packets, including the one that happens when you click on a packet, it can, for an SMB request, look up the response and see what the FID in the response was.</p></div><div id="comment-40824-info" class="comment-info"><span class="comment-age">(24 Mar '15, 20:48)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="40827"></span><div id="comment-40827" class="comment"><div id="post-40827-score" class="comment-score"></div><div class="comment-text"><p>I see. But if that is so, then why is it not able to get the FID in frame 292 when its there in the response?</p></div><div id="comment-40827-info" class="comment-info"><span class="comment-age">(24 Mar '15, 22:46)</span> <span class="comment-user userinfo">xerocool</span></div></div></div><div id="comment-tools-40818" class="comment-tools"></div><div class="clear"></div><div id="comment-40818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

