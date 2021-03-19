+++
type = "question"
title = "How does wireshark detects online-messenger traffic?"
description = '''I have been working on how to find use of online messenger (e.g imo.im, ebuddy) using wireshark. I&#x27;m doing , as i need to build SIEM (security information event management) use-cases which detects usage of online web-messenger.  To do little about of research, i went on a few online web-messenger an...'''
date = "2013-01-24T10:32:00Z"
lastmod = "2013-01-24T18:08:00Z"
weight = 17937
keywords = [ "expert-info" ]
aliases = [ "/questions/17937" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How does wireshark detects online-messenger traffic?](/questions/17937/how-does-wireshark-detects-online-messenger-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17937-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been working on how to find use of online messenger (e.g imo.im, ebuddy) using wireshark. I'm doing , as i need to build SIEM (security information event management) use-cases which detects usage of online web-messenger.</p><p>To do little about of research, i went on a few online web-messenger and turned on the wireshark in the background. After a couple of minutes of browsing the online messenger sites , i stopped the wireshark and went straight on analysis. At first, I found nothing special / unique which tells me (as a user) an online messaging service / protocol i used as all these sites works on http or https.</p><p>However, as i dig deep i find something interesting. The reference is given below:-</p><pre><code>Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        **[Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]**
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Encoding: gzip\r\n
    Cache-Control: max-age=10800\r\n
    Content-Type: text/html; charset=utf-8\r\n
    Date: Thu, 24 Jan 2013 17:58:46 GMT\r\n
    Expires: Thu, 24 Jan 2013 20:58:46 GMT\r\n
    Last-Modified: Thu, 24 Jan 2013 01:07:06 GMT\r\n
    p3p: CP=&quot;IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT&quot;\r\n
    Server: ECS (fra/D439)\r\n
    SVR: SP002B7\r\n
    Vary: Accept-Encoding\r\n
    X-Cache: HIT\r\n
    Content-Length: 387\r\n
    \r\n
    Content-encoded entity body (gzip): 387 bytes -&gt; 942 bytes
    Line-based text data: text/html</code></pre><p>I have searched the src code and beside PI_CHAT constant declaration in header file expert.c. If i follow the code in packet-http.c I see the following code.</p><pre><code>saw_req_resp_or_header = TRUE;
        if (is_request_or_reply) {
                char *text = tvb_format_text(tvb, offset, next_offset - offset);
            if (tree) {
                hdr_item = proto_tree_add_text(http_tree, tvb,
                    offset, next_offset - offset, &quot;%s&quot;, text);
            }
            expert_add_info_format(pinfo, hdr_item, PI_SEQUENCE, PI_CHAT, &quot;%s&quot;, text);
            if (reqresp_dissector) {
                if (tree) req_tree = proto_item_add_subtree(hdr_item, ett_http_request);
                else req_tree = NULL;

                reqresp_dissector(tvb, req_tree, offset, line,
                          lineend, conv_data);</code></pre><p>From the code above its hard to comprehend as to what conditions or input brings PI_CHAT variable to be set. Beside code , if anyone can explain in terms of theory as to how wireshark detects chatting behavior. The theory I have read on the wireshark official sites says expert info is to detect changes which are abnormal / anomalies in nature. I'm more interested in knowing the 'how' part.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">expert-info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p>lazerz<br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '13, 11:47</p></div></div><div id="comments-container-17937" class="comments-container"><span id="17938"></span><div id="comment-17938" class="comment"><div id="post-17938-score" class="comment-score"></div><div class="comment-text"><p>PI_CHAT refers to rhe severity level of the expert info.</p></div><div id="comment-17938-info" class="comment-info"><span class="comment-age">(24 Jan '13, 11:49)</span> Anders ♦</div></div></div><div id="comment-tools-17937" class="comment-tools"></div><div class="clear"></div><div id="comment-17937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17947"></span>

<div id="answer-container-17947" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17947-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As noted, "Chat" there means that Wireshark is just casually "chatting" to the user about stuff it's seeing, such as HTTP requests and responses; it has nothing whatsoever to do with instant messaging. There are several levels of expert info:</p><ul><li>"Comment" - packet is commented by the user</li><li>"Chat" - usual workflow, e.g. TCP connection establishing</li><li>"Note" - notable messages, e.g. an application returned an "usual" error code like HTTP 404</li><li>"Warning" - warning, e.g. application returned an "unusual" error code</li><li>"Error" - serious problems, e.g. [Malformed Packet]</li></ul><p>I've created <a href="http://ask.wireshark.org/questions/17939/using-wireshark-how-can-you-tell-whether-an-instant-message-website-has-been-accessed">a separate question</a> for your question about how, using Wireshark, you can tell whether an IM Website has been accessed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17947" class="comments-container"><span id="17984"></span><div id="comment-17984" class="comment"><div id="post-17984-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris. Thank you indeed for clearing the confusion. I appreciate very much that you created a separate question to entertain my query.Very helpful indeed. Thanks:)</p></div><div id="comment-17984-info" class="comment-info"><span class="comment-age">(27 Jan '13, 08:00)</span> lazerz</div></div></div><div id="comment-tools-17947" class="comment-tools"></div><div class="clear"></div><div id="comment-17947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

