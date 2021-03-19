+++
type = "question"
title = "Finding an rogue IP address"
description = '''Hi All,  Please forgive me, my IP and network knowledge is very limited. I occasionally work in a factory refurbishing second hand IP security equipment (cameras, NVRs etc). The equipment is not usually marked where they came from, and are very difficult to default back to factory presets (you have ...'''
date = "2014-03-27T08:12:00Z"
lastmod = "2014-03-27T11:36:00Z"
weight = 31218
keywords = [ "scanning", "ip", "address" ]
aliases = [ "/questions/31218" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Finding an rogue IP address](/questions/31218/finding-an-rogue-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31218-score" class="post-score" title="current number of votes">0</div><span id="post-31218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, Please forgive me, my IP and network knowledge is very limited. I occasionally work in a factory refurbishing second hand IP security equipment (cameras, NVRs etc). The equipment is not usually marked where they came from, and are very difficult to default back to factory presets (you have to pull the cases apart, and use a null modem serial cable and use lynx commands to default them which takes ages - and you have to default it, you can't change the ip address using this method). I'm hoping that there is a way that I can plug these devices in to the existing network and scan for and identify the device's IP address, so that I can re-program it using a web interface. Can wireshark do this maybe with filtering commands or is there another product that I can use maybe?</p><p>thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-scanning" rel="tag" title="see questions tagged &#39;scanning&#39;">scanning</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/e2c4968e8401dfb52ea6bfca16281c2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Green&#39;s gravatar image" /><p><span>John Green</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Green has no accepted answers">0%</span></p></div></div><div id="comments-container-31218" class="comments-container"></div><div id="comment-tools-31218" class="comment-tools"></div><div class="clear"></div><div id="comment-31218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31220"></span>

<div id="answer-container-31220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31220-score" class="post-score" title="current number of votes">0</div><span id="post-31220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A simple way to do this would be to connect it with a cross-cable directly to the laptop, or to connect it to a little hub. Make Wireshark sniff for traffic and if you're lucky you should see traffic coming from the camera. No device (that I know of) is completely quiet on the network. They're always searching for DNS-servers, a default gateway, websites to check for software updates, ARP-requests for all this, etc.</p><p>You'll also see some garbage coming from your own laptop, but it shouldn't be too difficult to see what is your own traffic, and what is not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/c27c52191553b276cf576ccd38f7ab3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robstar&#39;s gravatar image" /><p><span>robstar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robstar has no accepted answers">0%</span></p></div></div><div id="comments-container-31220" class="comments-container"></div><div id="comment-tools-31220" class="comment-tools"></div><div class="clear"></div><div id="comment-31220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31221"></span>

<div id="answer-container-31221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31221-score" class="post-score" title="current number of votes">0</div><span id="post-31221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you do this on a regular basis it's likely worth investing in a <a href="http://wiki.wireshark.org/TapReference">small aggregating tap</a> or a cheap switch that <a href="http://wiki.wireshark.org/SwitchReference">supports port mirroring</a> to passively capture the device's traffic. This will quickly show you any traffic generated by the device including its IP address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-31221" class="comments-container"><span id="31222"></span><div id="comment-31222" class="comment"><div id="post-31222-score" class="comment-score"></div><div class="comment-text"><p>While this is true it's not necessary in this case, because the IP security equipment doesn't work yet (it still needs to be reconfigured). So a simple cross cable already does the trick of discovering the IP-address of the device.</p><p>But yes, if John thinks he might need to troubleshoot while the device is actually active (and working) these things are better. But John says his knowledge about these things is very limited.</p><p>John, don't forget you need to reconfigure the IP-address of your laptop if you want to be able to actually reach the equipment. The IP of your laptop needs to be in the same subnet. (just saying)</p></div><div id="comment-31222-info" class="comment-info"><span class="comment-age">(27 Mar '14, 09:01)</span> <span class="comment-user userinfo">robstar</span></div></div></div><div id="comment-tools-31221" class="comment-tools"></div><div class="clear"></div><div id="comment-31221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31228"></span>

<div id="answer-container-31228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31228-score" class="post-score" title="current number of votes">0</div><span id="post-31228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and you have to default it, you can't change the ip address using this method</p></blockquote><p>I don't see how it will help you to figure out the IP address. If the address is not set to a default value, it is very likely that the username/password has been changed as well.</p><blockquote><p>scan for and identify the device's IP address, so that I can re-program it using a web interface.</p></blockquote><p>well, you might be able to access the web interface, but you (probably) won't be able to log in as you don't know the username and password, unless those devices offer a secret/hidden 'reset the device without admin credentials' URL (which I doubt).</p><p>So, sorry but I think you'll have to walk the bumpy road....</p><p>Look at it this way: That amount of work you have to invest is the value you add to those refurbished devices ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31228" class="comments-container"></div><div id="comment-tools-31228" class="comment-tools"></div><div class="clear"></div><div id="comment-31228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

