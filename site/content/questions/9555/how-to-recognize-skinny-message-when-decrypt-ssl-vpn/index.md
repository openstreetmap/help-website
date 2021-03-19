+++
type = "question"
title = "how to recognize skinny message when decrypt ssl vpn"
description = '''The scenario is that I use openconnect to connect cisco phone to cisco IOS&#x27;s sslvpn server. phone will be registered to the call manager and the call manager communicate with phone using skinny msg. I already have the private key of the sslvpn server and use it in wireshark. My wireshark&#x27;s version i...'''
date = "2012-03-15T06:49:00Z"
lastmod = "2012-03-15T06:49:00Z"
weight = 9555
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/9555" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to recognize skinny message when decrypt ssl vpn](/questions/9555/how-to-recognize-skinny-message-when-decrypt-ssl-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9555-score" class="post-score" title="current number of votes">0</div><span id="post-9555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The scenario is that I use openconnect to connect cisco phone to cisco IOS's sslvpn server.</p><p>phone will be registered to the call manager and the call manager communicate with phone using skinny msg.</p><p>I already have the private key of the sslvpn server and use it in wireshark.</p><p>My wireshark's version is 1.6.5 My setting is that:</p><p>Preferences-&gt;Protocols-&gt;SSL</p><p>IP address is set to the sslvpn server's ip.</p><p>port is set to 443</p><p>Protocol is set to http</p><p>key is the location of the private key.</p><p>I found that I can see some http msg decrypted using this setting.(without the private key, the http msg can not be seen.)</p><p>But other msg is still "TLSv1 Application Data".(should be skinny msg)</p><p>I try to set to change ssl decrypt protocol from ”http“ to "skinny"</p><p>the error shows that "error in column 'Protocol': Could not find dissector for: 'skinny'"</p><p>I try to set "http" to "tcp" and there is some tcp.</p><p>So is there a way to decrypt these Application Data to right skinny msg?</p><p>Thanks for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '12, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/9f4490adb1eec68f30f8022303c26971?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varvar&#39;s gravatar image" /><p><span>varvar</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varvar has no accepted answers">0%</span></p></div></div><div id="comments-container-9555" class="comments-container"></div><div id="comment-tools-9555" class="comment-tools"></div><div class="clear"></div><div id="comment-9555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

