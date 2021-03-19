+++
type = "question"
title = "sniff a facebook password"
description = '''can i sniff a Facebook password or hotmail password??? thanks'''
date = "2014-01-07T12:05:00Z"
lastmod = "2014-08-21T00:39:00Z"
weight = 28647
keywords = [ "facebook" ]
aliases = [ "/questions/28647" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [sniff a facebook password](/questions/28647/sniff-a-facebook-password)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28647-score" class="post-score" title="current number of votes">0</div><span id="post-28647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can i sniff a Facebook password or hotmail password???</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-facebook" rel="tag" title="see questions tagged &#39;facebook&#39;">facebook</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/2f71902b61e9ff0244b76254eadfd590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobsta&#39;s gravatar image" /><p><span>bobsta</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobsta has no accepted answers">0%</span></p></div></div><div id="comments-container-28647" class="comments-container"></div><div id="comment-tools-28647" class="comment-tools"></div><div class="clear"></div><div id="comment-28647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="28651"></span>

<div id="answer-container-28651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28651-score" class="post-score" title="current number of votes">1</div><span id="post-28651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. But you probably can't read it because it is usually encrypted in an HTTPS conversation. If you have the decryption key for SSL you could have Wireshark decode the communication after capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28651" class="comments-container"></div><div id="comment-tools-28651" class="comment-tools"></div><div class="clear"></div><div id="comment-28651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28667"></span>

<div id="answer-container-28667" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28667-score" class="post-score" title="current number of votes">1</div><span id="post-28667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>can i sniff a Facebook password or hotmail password???</p></blockquote><p>the password for both are transmitted via encrypted channels and you won't be able to decrypt that connection, unless you</p><ol><li>own the crypto keys of facebook and/or hotmail servers</li><li>are able to export the SSL/TLS session keys in your SSL/TLS client (browser, app, etc.) and use those keys to decrypt the session with Wireshark</li><li>are able to intercept the SSL/TLS connection with something like <a href="http://fiddler2.com/">Fiddler</a></li></ol><p>You did not say, if you want to sniff the password transmission of <strong>your own</strong> system or a <strong>remote system</strong>!</p><p>So, let's see:</p><p>1.) is rather unlikely, unless</p><ul><li>you are a <strong>very gifted</strong> hacker</li><li>you own the <strong>vast majority</strong> of shares of either company</li><li>you have <strong>very good</strong> contacts to the NSA</li><li>you can <strong>bribe or blackmail</strong> one of the server admins</li></ul><p>2.) will work</p><ul><li>on <strong>your own</strong> system, if your client software supports the export of the session keys (some browsers do, most other software don't).<br />
</li><li>on a <strong>remote system</strong>, if you are able to install some modified software on the system of your target person. However, if you are able to <strong>do that</strong>, there is <strong>no need to 'sniff'</strong> the password ;-)</li></ul><p>3.) will work</p><ul><li>on <strong>your own</strong> system, by installing and using tools like <a href="http://fiddler2.com/">Fiddler</a></li><li>for a <strong>remote system</strong>, if you have access to major parts of the network of your target person. However, if you have that kind of access, there is probably no need to 'sniff' the password as well ;-)</li></ul><p>Good luck!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '14, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jan '14, 08:53</strong> </span></p></div></div><div id="comments-container-28667" class="comments-container"></div><div id="comment-tools-28667" class="comment-tools"></div><div class="clear"></div><div id="comment-28667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35649"></span>

<div id="answer-container-35649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35649-score" class="post-score" title="current number of votes">0</div><span id="post-35649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Cookies...cookies :) Spoffing cookies is the best method to get into someone account. If you get cookies you can dump into your browser and use it to autenthication into maybe facebook. Or if you fast computer and advence skill in programming. You can use cuda or some server to decrypt password. This is very brutal and long operation. Although you have big base with rainbow tables. Its take in the most optimistic scenario about few days.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '14, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/668efb8433e5e9fa56660b80c42b9d6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkubasz&#39;s gravatar image" /><p><span>mkubasz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkubasz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '14, 00:45</strong> </span></p></div></div><div id="comments-container-35649" class="comments-container"></div><div id="comment-tools-35649" class="comment-tools"></div><div class="clear"></div><div id="comment-35649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

