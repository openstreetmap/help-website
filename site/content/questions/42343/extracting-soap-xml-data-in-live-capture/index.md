+++
type = "question"
title = "Extracting SOAP XML data in live capture"
description = '''Greetings all, I am new to Lua and Wireshark together so apologies for my first post. The situation I have is that we have a server which is pumping out notifications using SOAP/XML protocol. The notification messages are very small in size and coming out at a rate of 10-20 per minute. Initially I w...'''
date = "2015-05-12T12:26:00Z"
lastmod = "2015-05-20T14:40:00Z"
weight = 42343
keywords = [ "xml", "lua", "soap", "wireshark" ]
aliases = [ "/questions/42343" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting SOAP XML data in live capture](/questions/42343/extracting-soap-xml-data-in-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42343-score" class="post-score" title="current number of votes">0</div><span id="post-42343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings all,</p><p>I am new to Lua and Wireshark together so apologies for my first post.</p><p>The situation I have is that we have a server which is pumping out notifications using SOAP/XML protocol. The notification messages are very small in size and coming out at a rate of 10-20 per minute.</p><p>Initially I wrote a Lua script (after researching for several hours) to extract the data I needed (link below).</p><p><a href="http://www.pastebin.ca/3001877">XML Payload and Lua script</a></p><p>After executing the script I get output as follows</p><pre><code>State Change detected
Object Instance              = 43606
Attribute Value Change Type  = OperationalState
Attribute Value Change Value = DISABLED
tap.packet      #279
Attribute Value Change detected
Object Instance              = 43606
Attribute Value Change Type  = 1475
Attribute Value Change Value = ENABLED
tap.packet      #281
State Change detected
Object Instance              = 43606
Attribute Value Change Type  = OperationalState
Attribute Value Change Value = ENABLED
tap.packet      #283
tap.packet      #286
tap.packet      #288
Attribute Value Change detected
Object Instance              = 230690
Attribute Value Change Type  = 4060
Attribute Value Change Value = REGISTERED</code></pre><p>What I want to next is make the same output appear in a text window within Wireshark GUI. The linked Lua script does not work in a Wireshark Menu wrapper as <strong>Field</strong> is not available.</p><p>I would love to hear some pointers or tips on how to proceed. I'm not familiar with writing dissectors if that is the path I need to take..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '15, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/8e191d3ad5ed97a4ab999dfe6087ae92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlwain74&#39;s gravatar image" /><p><span>carlwain74</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlwain74 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '15, 02:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42343" class="comments-container"></div><div id="comment-tools-42343" class="comment-tools"></div><div class="clear"></div><div id="comment-42343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42384"></span>

<div id="answer-container-42384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42384-score" class="post-score" title="current number of votes">0</div><span id="post-42384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Carl,</p><p>You'd need to start your script in the same way you are starting tshark that is with -X option.</p><p>If I recall correctly Field is not available if you simply paste the code into eval window of wireshark after it was started.</p><p>Rather than printing you may want to add text to info column ( something along the lines )</p><pre><code>pinfo.cols.info = objInst .. &quot; &quot; .. attrType</code></pre><p>Or you may want to use info('') instead of print this will show up in the console ( you may have to reload your pcap after console is opened.</p><p>Regards</p><p>Marcin</p><p>p.s. Nice to see you are still tinkering with lua ;-) good old IPA days</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '15, 03:17</strong> </span></p></div></div><div id="comments-container-42384" class="comments-container"><span id="42593"></span><div id="comment-42593" class="comment"><div id="post-42593-score" class="comment-score"></div><div class="comment-text"><p>For some reason not all the XML is being made available. When I finally get to examine the XML content for a different message I am only getting the second half of the XML payload.</p></div><div id="comment-42593-info" class="comment-info"><span class="comment-age">(20 May '15, 14:40)</span> <span class="comment-user userinfo">carlwain74</span></div></div></div><div id="comment-tools-42384" class="comment-tools"></div><div class="clear"></div><div id="comment-42384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42398"></span>

<div id="answer-container-42398" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42398-score" class="post-score" title="current number of votes">0</div><span id="post-42398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Marcin,</p><p>Good to hear your still out there working with Wireshark..</p><p>It actually worked out that I did not need the Field code to get it to work. The following line was enough to get what I needed. I just needed to offset the XML payload and 50 seemed to work fine and now I can decode all XML payloads.</p><pre><code> local xmldata   = tvb(50):string()</code></pre><p>Now I'm stuck on another issue opening a simple filename.</p><p>Carl</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/8e191d3ad5ed97a4ab999dfe6087ae92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlwain74&#39;s gravatar image" /><p><span>carlwain74</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlwain74 has no accepted answers">0%</span></p></div></div><div id="comments-container-42398" class="comments-container"></div><div id="comment-tools-42398" class="comment-tools"></div><div class="clear"></div><div id="comment-42398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

