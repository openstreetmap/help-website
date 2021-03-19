+++
type = "question"
title = "Google Analytics in native apps (iPad)"
description = '''Scenario: iPad app with Analytics SDK installed. Data is coming in, reports are showing up with reasonable numbers. However I need to debug single requests Analytics is doing, to make sure, every information bit is send with the right info. Setup is a win7 machine with latest Wireshark. Ad Hoc netwo...'''
date = "2013-09-20T01:14:00Z"
lastmod = "2013-09-20T05:28:00Z"
weight = 24985
keywords = [ "ipad", "analytics", "app", "google" ]
aliases = [ "/questions/24985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Google Analytics in native apps (iPad)](/questions/24985/google-analytics-in-native-apps-ipad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24985-score" class="post-score" title="current number of votes">0</div><span id="post-24985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Scenario: iPad app with Analytics SDK installed. Data is coming in, reports are showing up with reasonable numbers. However I need to debug single requests Analytics is doing, to make sure, every information bit is send with the right info. Setup is a win7 machine with latest Wireshark. Ad Hoc network, where an iPad is dialing up to get WiFi access through my laptops connection. It works fine: with Wireshark filter http.request.full_uri contains "__utm.gif" I can easily see requests made in Safari Browser on the iPad. It shows up exactly as supposed, a simple HTTP request.</p><p>Now I start the app on the iPad and it is the one, reporting data to Analytics. However I can't find any filter to get to the packages, send by Analytics SDK. Now I also tested Fiddler (and Charles on Mac, too) as a Proxy, both tools show a SSL connection to www.google-analytics.com. However with no information about the tracking.</p><p>Do you have any hints how to set up a filter to see data transfer from the app, where Analytics is sending data to its servers?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipad" rel="tag" title="see questions tagged &#39;ipad&#39;">ipad</span> <span class="post-tag tag-link-analytics" rel="tag" title="see questions tagged &#39;analytics&#39;">analytics</span> <span class="post-tag tag-link-app" rel="tag" title="see questions tagged &#39;app&#39;">app</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/0f206c1ef78a7ea864fd697f05f5e1e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mischa&#39;s gravatar image" /><p><span>Mischa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mischa has no accepted answers">0%</span></p></div></div><div id="comments-container-24985" class="comments-container"></div><div id="comment-tools-24985" class="comment-tools"></div><div class="clear"></div><div id="comment-24985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24986"></span>

<div id="answer-container-24986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24986-score" class="post-score" title="current number of votes">2</div><span id="post-24986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>both tools <strong>show a SSL connection to www.google-analytics.com.</strong> Do you have any hints how to set up a filter to see data transfer from the app,</p></blockquote><p>if the traffic is encrypted, you cannot 'look' inside that connection with Wireshark, unless you are able to decrypt the conversation, which in turn is (almost) impossible, as you will have no access to the private keys of google.</p><p>The proposed way to use Fidler is the right way to proceed in your scenario. If Fiddler does not show anything, you need to tweak your Fiddler setup, however that's a thing you better discuss on a Fiddler forum.</p><p>Hint: There is a Fiddler plugin to generate PCAP files of the 'decrypted' conversation. You can use that capture file in Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24986" class="comments-container"><span id="24991"></span><div id="comment-24991" class="comment"><div id="post-24991-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for reply! <a href="http://fiddler2.com/add-ons">http://fiddler2.com/add-ons</a> There is sadly no add on which mentions PCAP.</p><p>Its not the right place to ask about fiddler, but maybe somebody can help: I see this information in Fiddler: Host = tunnel to URI = ssl.google-analytics.com:443</p><p>I configured decryption of this request. However, the only thing to see is the GET / request with no information bout parameters, send within the request. There must be the artifacts somewhere? In plain HTTP its just a part of the URI. Is it kind of hidden inside this SSL request?</p></div><div id="comment-24991-info" class="comment-info"><span class="comment-age">(20 Sep '13, 02:46)</span> <span class="comment-user userinfo">Mischa</span></div></div><span id="24994"></span><div id="comment-24994" class="comment"><div id="post-24994-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks so much for reply! <a href="http://fiddler2.com/add-ons">http://fiddler2.com/add-ons</a> There is sadly no add on which mentions PCAP.</p></blockquote><p>here we go: <a href="http://fiddler2.com/fiddlercap">http://fiddler2.com/fiddlercap</a></p><blockquote><p>I configured decryption of this request. However, the only thing to see is the GET / request</p></blockquote><p>Maybe your client on the iPad has problems with the intermediate certificate created by Fiddler and thus stops sending the "real" requests after some time.</p></div><div id="comment-24994-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24999"></span><div id="comment-24999" class="comment"><div id="post-24999-score" class="comment-score"></div><div class="comment-text"><p>The second comment seems correct. How can I make the iPad accept the intermediate certificated which is created by Fiddler? Any hint is very helpful. Thank you so far!</p></div><div id="comment-24999-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:15)</span> <span class="comment-user userinfo">Mischa</span></div></div><span id="25005"></span><div id="comment-25005" class="comment"><div id="post-25005-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How can I make the iPad accept the intermediate certificated which is created by Fiddler?</p></blockquote><p>I have no idea ;-) Maybe you'll have to import the cert somewhere. google or the fancy guys in the apple store will tell you. Just ask for: iPad certificate management</p><p>Anyway: What is the application on the iPad? System browser, some app (which one)?</p></div><div id="comment-25005-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25011"></span><div id="comment-25011" class="comment"><div id="post-25011-score" class="comment-score"></div><div class="comment-text"><p>I fixed it :)</p><p>it's very easy: on the iPad open <a href="http://ipv4.fiddler:8888/">http://ipv4.fiddler:8888/</a> and install Fiddlers Certificate. Thats it.</p><p>More Info: <a href="http://fiddler2.com/documentation/Configure-Fiddler/Tasks/ConfigureForiOS">http://fiddler2.com/documentation/Configure-Fiddler/Tasks/ConfigureForiOS</a></p><p>Thanks!</p></div><div id="comment-25011-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:44)</span> <span class="comment-user userinfo">Mischa</span></div></div><span id="25024"></span><div id="comment-25024" class="comment not_top_scorer"><div id="post-25024-score" class="comment-score"></div><div class="comment-text"><p><span>@Mischa</span> If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-25024-info" class="comment-info"><span class="comment-age">(20 Sep '13, 05:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-24986" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-24986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

