+++
type = "question"
title = "[closed] Unable to capture Facebook cookies"
description = '''HII...actually my wireshark is not capturing facebook packets..i have selected appropriate interface and filtered the screen by writing [http.cookies contains &quot;datr&quot;] but still it does n&#x27;t show any captured cookie..plzz help me'''
date = "2015-06-30T09:43:00Z"
lastmod = "2015-06-30T09:50:00Z"
weight = 43734
keywords = [ "sniffing", "facebook", "cookie" ]
aliases = [ "/questions/43734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Unable to capture Facebook cookies](/questions/43734/unable-to-capture-facebook-cookies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HII...actually my wireshark is not capturing facebook packets..i have selected appropriate interface and filtered the screen by writing [http.cookies contains "datr"] but still it does n't show any captured cookie..plzz help me</p></div><div id="question-tags" class="tags-container tags">sniffing facebook cookie</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/c68ff39b71ce68c21632265b12250752?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karamveer%20Singh&#39;s gravatar image" /><p>Karamveer Singh<br />
<span class="score" title="-1 reputation points">-1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karamveer Singh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 01 Jul '15, 04:32</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43734" class="comments-container"></div><div id="comment-tools-43734" class="comment-tools"></div><div class="clear"></div><div id="comment-43734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Actual question is about hacking Facebook accounts" by grahamb 01 Jul '15, 04:32

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43736"></span>

<div id="answer-container-43736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check if you have packets being sent to the Facebook IP at all, and what port it is. My guess is that it'll show as TCP port 443, which would mean HTTPS. Which would mean the communication is encrypted. Which would mean you can't read anything, including cookies. So filters for HTTP cookies won't work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-43736" class="comments-container"><span id="43737"></span><div id="comment-43737" class="comment"><div id="post-43737-score" class="comment-score"></div><div class="comment-text"><p>so what i have to do for capturing facebook cookies</p></div><div id="comment-43737-info" class="comment-info"><span class="comment-age">(30 Jun '15, 09:52)</span> Karamveer Singh</div></div><span id="43738"></span><div id="comment-43738" class="comment"><div id="post-43738-score" class="comment-score"></div><div class="comment-text"><p>Depends. If it is your own traffic you could try to decode the encryption. There are some articles and tutorials on how to do that with Wireshark, but you'll need session or server keys.</p><p>If it's not your traffic and have no access to the secret keys the answer is simple: you can't do anything.</p></div><div id="comment-43738-info" class="comment-info"><span class="comment-age">(30 Jun '15, 09:56)</span> Jasper ♦♦</div></div><span id="43739"></span><div id="comment-43739" class="comment"><div id="post-43739-score" class="comment-score"></div><div class="comment-text"><p>Run the connection through a MITM proxy such as Fiddler to get the decrypted stream. See <a href="http://www.fiddlerbook.com/fiddler/help/httpsdecryption.asp">http://www.fiddlerbook.com/fiddler/help/httpsdecryption.asp</a> for more info.</p></div><div id="comment-43739-info" class="comment-info"><span class="comment-age">(30 Jun '15, 09:58)</span> grahamb ♦</div></div><span id="43740"></span><div id="comment-43740" class="comment"><div id="post-43740-score" class="comment-score"></div><div class="comment-text"><p>ok but i hve seen some videos ...in that they easily use to capture facebook packets by writing the same thing that i have written...why they are able to capture?</p></div><div id="comment-43740-info" class="comment-info"><span class="comment-age">(30 Jun '15, 09:59)</span> Karamveer Singh</div></div><span id="43741"></span><div id="comment-43741" class="comment"><div id="post-43741-score" class="comment-score"></div><div class="comment-text"><p>What date do they have? Likely that they are old and from prehistoric times when we didn't use HTTPS everywhere.</p></div><div id="comment-43741-info" class="comment-info"><span class="comment-age">(30 Jun '15, 10:28)</span> grahamb ♦</div></div><span id="43772"></span><div id="comment-43772" class="comment not_top_scorer"><div id="post-43772-score" class="comment-score"></div><div class="comment-text"><p>okay....so i can hack any fb account withe the help of wireshark or not...if yes then plzz send the link</p></div><div id="comment-43772-info" class="comment-info"><span class="comment-age">(01 Jul '15, 02:42)</span> Karamveer Singh</div></div><span id="43777"></span><div id="comment-43777" class="comment not_top_scorer"><div id="post-43777-score" class="comment-score"></div><div class="comment-text"><p>You'll have to go and look elsewhere for Facebook account hacks.</p></div><div id="comment-43777-info" class="comment-info"><span class="comment-age">(01 Jul '15, 04:31)</span> grahamb ♦</div></div></div><div id="comment-tools-43736" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-43736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

