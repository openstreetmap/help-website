+++
type = "question"
title = "lua tap for bundled packets"
description = '''Hi,  Lets say I have a packet that looks like this :  [ETH, IP, HEADER, PAYLOAD, HEADER, PAYLOAD] My Header consists of header.x1 header.x2 and header.x3 and payload is payload.x1 and payload.x2.  I want to use a lua tap to calculate how many [header, payload] packets a file consists of. So in this ...'''
date = "2013-04-22T02:01:00Z"
lastmod = "2013-04-23T00:39:00Z"
weight = 20696
keywords = [ "lua", "tap", "unbundle", "bundling" ]
aliases = [ "/questions/20696" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lua tap for bundled packets](/questions/20696/lua-tap-for-bundled-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20696-score" class="post-score" title="current number of votes">0</div><span id="post-20696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Lets say I have a packet that looks like this :</p><p>[ETH, IP, HEADER, PAYLOAD, HEADER, PAYLOAD]</p><p>My Header consists of header.x1 header.x2 and header.x3 and payload is payload.x1 and payload.x2.</p><p>I want to use a lua tap to calculate how many [header, payload] packets a file consists of. So in this case, it is just one IP packet, but consist of two packets with [header, payload]. I have a lua tap that goes like this :</p><p>-- simple_http.lua</p><p>-- implements a very simple tap in Lua</p><p>-- this is going to be our counter</p><p>http_packets = 0</p><p>-- this is going to be our tap</p><p>tap_http = nil</p><p>-- first we declare the tap called "http tap" with the filter it is going to use</p><p>tap_http = Listener.new(nil,"header.x1 == 2")</p><p>-- this function will get called at the end(3) of the capture to print the summary</p><p>function tap_http.draw()</p><pre><code>debug(&quot;http packets:&quot; .. http_packets)</code></pre><p>end</p><p>-- this function is going to be called once each time the filter of the tap matches</p><p>function tap_http.packet()</p><pre><code>http_packets = http_packets + 1</code></pre><p>end</p><p>-- this function will be called at the end of the capture run</p><p>function tap_http.reset()</p><pre><code>http_packets = 0</code></pre><p>end</p><p>Now the problem with this however, is that it will count the above packet only as +1. It will only read the first header.x1, and if this is 2 it will add +1. But if the other bundled header.x2 also is two, it will not be included in the calculation. How can I make this tap read all the budled packets from this IP packet?</p><p>Thank you very much in advance</p><p>BR Harkap</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-unbundle" rel="tag" title="see questions tagged &#39;unbundle&#39;">unbundle</span> <span class="post-tag tag-link-bundling" rel="tag" title="see questions tagged &#39;bundling&#39;">bundling</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p><span>harkap</span><br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span></p></div></div><div id="comments-container-20696" class="comments-container"></div><div id="comment-tools-20696" class="comment-tools"></div><div class="clear"></div><div id="comment-20696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20730"></span>

<div id="answer-container-20730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20730-score" class="post-score" title="current number of votes">0</div><span id="post-20730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd do it by using generic tap, and an extractor. Now depending on your protocol it will be either common extractor for same field type that returns a table or two separate extractors.</p><p>Code below is not tested but you should get the idea</p><pre><code>x1_extractor = Field.new(&quot;header.field1&quot;)
x2_extractor = Field.new(&quot;header.field2&quot;)
x3_common_extractor = Field.new(&quot;header.common_field3&quot;)
tap_http = Listener.new(nil,&quot;header&quot;)
http_packet=0
function tap_http.packet()
       x1_field = x1_extractor()
       x2_field = x2_extractor()
       -- For a common field in both instances use a table like below
       my_field_table = { x3_common_extractor() } 
       -- my_field_table[0].value - will give you falue from first instance
       -- my_field_table[0].value - will give you falue from second instance
       if x1_field and x1_field.value == 2 then
           http_packet = http_packet +1 
       end  

       if x2_field and x2_field.value == 2 then
           http_packet = http_packet +1 
       end  


end
</code></pre><p>Also: Check out this question: <a href="http://ask.wireshark.org/questions/4225/lua-how-to-get-multiple-values-from-faststart-items-h225-h245?page=1&amp;focusedAnswerId=4236#4236">How to get multiple values from items</a></p><p>Check out this question: <a href="http://ask.wireshark.org/questions/11000/lua-tap-and-multiple-instances-of-a-protocol-in-one-frame">Multiple instances of a protocol in one frame</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '13, 00:41</strong> </span></p></div></div><div id="comments-container-20730" class="comments-container"></div><div id="comment-tools-20730" class="comment-tools"></div><div class="clear"></div><div id="comment-20730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

