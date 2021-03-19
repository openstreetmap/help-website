+++
type = "question"
title = "How to decrypt SSL using DigiCert Root Certificate within HTTPS POST traffic from Java App?"
description = '''Hi I am able to capture traffic between a Java app using HttpsURLConnection POST to API endpoint https://int.tangocard.com For security, this endpoint uses a DigiCert Root Certificate. I tried adding this DigiCert Root Certificate to RSA Key List within SSL Protocol preferences, but that did not dec...'''
date = "2012-11-08T08:39:00Z"
lastmod = "2012-11-08T08:39:00Z"
weight = 15729
keywords = [ "ssl", "https", "certificate" ]
aliases = [ "/questions/15729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt SSL using DigiCert Root Certificate within HTTPS POST traffic from Java App?](/questions/15729/how-to-decrypt-ssl-using-digicert-root-certificate-within-https-post-traffic-from-java-app)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am able to capture traffic between a Java app using <strong>HttpsURLConnection POST</strong> to API endpoint <strong><a href="https://int.tangocard.com">https://int.tangocard.com</a></strong></p><p>For security, this endpoint uses a <strong>DigiCert Root Certificate</strong>.</p><p>I tried adding this <strong>DigiCert Root Certificate</strong> to <strong>RSA Key List</strong> within <strong>SSL Protocol preferences</strong>, but that did not decrypt <strong>Ecrypted Application Data</strong> within Secure Socket Layer of captured traffic.</p><p>Within aforementioned list, I added IP Address, Port <strong>443</strong>, Protocol <strong>http</strong>, File path to <strong>DigiCert Root Certificate</strong>.</p><p>Am I not performing decryption correctly?</p><p>Jeff in Seattle</p></div><div id="question-tags" class="tags-container tags">ssl https certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/d43e972a8ca84b9478a814f32e464fd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeff00tangocard&#39;s gravatar image" /><p>jeff00tangocard<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeff00tangocard has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '12, 08:41</p></div></div><div id="comments-container-15729" class="comments-container"><span id="15736"></span><div id="comment-15736" class="comment"><div id="post-15736-score" class="comment-score"></div><div class="comment-text"><p>I modified <strong><em>key file</em></strong> within <strong>RSA Key List</strong> to point to a <strong><em>cacert.pem</em></strong> file which does have <strong><em>DigiCert Root Certificate</em></strong>, but I am not seeing expected <strong><em>Decrypted SSL Data</em></strong>.</p><p>Where would I find this?</p><p>Jeff in Seattle</p></div><div id="comment-15736-info" class="comment-info"><span class="comment-age">(08 Nov '12, 09:18)</span> jeff00tangocard</div></div></div><div id="comment-tools-15729" class="comment-tools"></div><div class="clear"></div><div id="comment-15729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

