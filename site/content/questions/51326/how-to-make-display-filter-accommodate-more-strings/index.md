+++
type = "question"
title = "How To Make Display Filter Accommodate More Strings"
description = '''Hi For SIP, I&#x27;ll like to separate Rejected Calls, Cancelled Calls and Completed Calls and save as separate trace captures. So on menu, I open the &#x27;Telephony --&amp;gt; VoIP Calls&#x27;. I sort by State. Highlight all Rejected Calls [as an example] and click &#x27;prepare filter&#x27; button. Wireshark prepares the fil...'''
date = "2016-03-31T18:44:00Z"
lastmod = "2016-04-09T03:59:00Z"
weight = 51326
keywords = [ "sip", "voip" ]
aliases = [ "/questions/51326" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How To Make Display Filter Accommodate More Strings](/questions/51326/how-to-make-display-filter-accommodate-more-strings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51326-score" class="post-score" title="current number of votes">1</div><span id="post-51326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi For SIP, I'll like to separate Rejected Calls, Cancelled Calls and Completed Calls and save as separate trace captures. So on menu, I open the 'Telephony --&gt; VoIP Calls'. I sort by State. Highlight all Rejected Calls [as an example] and click 'prepare filter' button. Wireshark prepares the filter based on Call ID. For very long filter strings, it shows red. It appears Wireshark has a LIMIT to the display filter string. Please how do I increase it, so that the display filter accepts more string?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_Filter.jpg" alt="alt text" /></p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '16, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/b744fd9e3ba26e0b8dd665574773e5d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EmaX&#39;s gravatar image" /><p><span>EmaX</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EmaX has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '16, 18:53</strong> </span></p></div></div><div id="comments-container-51326" class="comments-container"><span id="51409"></span><div id="comment-51409" class="comment"><div id="post-51409-score" class="comment-score">1</div><div class="comment-text"><p>As a workaround you can use <code>sip.Call-ID contains "(subset of Call-ID)"</code> instead of a full match with <code>sip.Call-ID == "..."</code>.</p></div><div id="comment-51409-info" class="comment-info"><span class="comment-age">(05 Apr '16, 01:50)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="51465"></span><div id="comment-51465" class="comment"><div id="post-51465-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response Lekensteyn. But it's not clear to me what you mean.</p><p>I have a trace capture I want to analyze. Contains about 100,000 calls. To help me understand, please can you give an example of how I could use <strong><em>sip.Call-ID contains "(subset of Call-ID)" instead of a full match with sip.Call-ID == "...".</em></strong></p><p>Thanks</p></div><div id="comment-51465-info" class="comment-info"><span class="comment-age">(07 Apr '16, 05:37)</span> <span class="comment-user userinfo">EmaX</span></div></div></div><div id="comment-tools-51326" class="comment-tools"></div><div class="clear"></div><div id="comment-51326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51528"></span>

<div id="answer-container-51528" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51528-score" class="post-score" title="current number of votes">1</div><span id="post-51528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="EmaX has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While this is not an answer to the exact wording of your question, it could be an answer to your actual need. You may use MATE to augment all SIP messages belonging to a given SIP dialog with the response code to the initial INVITE of that dialog, and then use this pseudo-field in display filter to display all messages of all dialogs whose initial INVITE has been responded by a given response. So you would e.g. use <code>mate.sip_dialog.rsp_code == 486</code> to display only messages belonging to SIP dialogs which have failed with "busy here".</p><p>The mate configuration looks as follows:</p><pre><code>Transform rmv_rq_cseq {
    Match (to_tag, rq_cseq) Replace ();
    Match (method=&quot;INVITE&quot;);
    Match (rq_cseq) Replace ();
};

Transform rmv_low_rc {
    Match (rsp_code^&quot;1&quot;) Replace ();
    Match (rsp_code=&quot;401&quot;) Replace ();
    Match (rsp_code=&quot;407&quot;) Replace ();
};

Transform rmv_rsp_code {
    Match (rq_cseq);
    Match (rsp_code) Replace (); 
};

Pdu sip_pdu Proto sip Transport ip {
    Extract rsp_code From sip.Status-Code;
    Extract call_id From sip.Call-ID;
    Extract rq_cseq From sip.CSeq.seq;
    Extract method From sip.Method;
    Extract to_tag From sip.to.tag;
    Extract cseq From sip.CSeq;
    Transform rmv_rq_cseq, rmv_low_rc;
};

Gop sip_xaction On sip_pdu Match (call_id,cseq) {
    Start (method);
    Stop (rsp_code);
    Extra (call_id, rq_cseq, rsp_code);
    Transform rmv_rsp_code;
};

Gog sip_dialog {
    Member sip_xaction (call_id);
    Extra (rsp_code);
    Expiration 86400.0;
};</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '16, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Apr '16, 09:14</strong> </span></p></div></div><div id="comments-container-51528" class="comments-container"></div><div id="comment-tools-51528" class="comment-tools"></div><div class="clear"></div><div id="comment-51528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51524"></span>

<div id="answer-container-51524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51524-score" class="post-score" title="current number of votes">0</div><span id="post-51524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The generated display filter is too long, as a workaround you can try to replace long filters such as</p><pre><code> (sip.Call-ID == &quot;40befb2f61f6f2021ed5&quot;) or (sip.Call-ID == &quot;233bc04c777e49e8e81e&quot;)</code></pre><p>by this filter (where the Call IDs are abbreviated to a substring):</p><pre><code>(sip.Call-ID contains &quot;40befb2f&quot;) or (sip.Call-ID contains &quot;233bc04c&quot;)</code></pre><p>The string can even be shortened further using a regular expression:</p><pre><code>sip.Call-ID matches &quot;(40befb2f|233bc04c)&quot;</code></pre><p>The first to second conversion can be done with this <a href="https://www.python.org/">Python</a> script (save as <code>short.py</code> for example):</p><pre><code>#!/usr/bin/env python
# Reads the display filter from console (standard input) and shortens Call-IDs
# to the first 10 characters (see begin and length parameters below).
import sys, re
begin = 0
length = 10
line = sys.stdin.readline()
def repl(match):
    return &#39;sip.Call-ID contains &quot;%s&quot;&#39; % match.group(1)[begin:begin+length]
print(re.sub(&#39;sip.Call-ID == &quot;([^&quot;]+)&quot;&#39;, repl, line))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-51524" class="comments-container"><span id="51525"></span><div id="comment-51525" class="comment"><div id="post-51525-score" class="comment-score"></div><div class="comment-text"><p>Thanks Again But one last question.</p><p>I installed Python, path correct, watched a <a href="https://www.youtube.com/watch?v=6ZpuwW-9T54">youtube vid</a> that shows how to run it on sublime text. The thing is where do i store the prepared filter? i.e. what's the easiest way to get it done with python? You could please point me to a video that explains it... Thanks</p></div><div id="comment-51525-info" class="comment-info"><span class="comment-age">(08 Apr '16, 17:09)</span> <span class="comment-user userinfo">EmaX</span></div></div><span id="51530"></span><div id="comment-51530" class="comment"><div id="post-51530-score" class="comment-score">1</div><div class="comment-text"><p>Once you run the script, you can paste the original display filter. Then copy the result and replace the original filter.</p></div><div id="comment-51530-info" class="comment-info"><span class="comment-age">(09 Apr '16, 03:59)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-51524" class="comment-tools"></div><div class="clear"></div><div id="comment-51524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

