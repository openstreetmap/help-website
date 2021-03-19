+++
type = "question"
title = "Wireshark Mate Gop&#x27;s not collected in same Gog."
description = '''Hi! I&#x27;m trying to use Mate to collect SIP and Megaco messages. This has been tried by a number of times as it exist a number of questions on the web, but I have not get any answer. I have the following Mate configuration: Pdu sip_msg Proto sip Transport ip {  Extract sip_callid From sip.Call-ID;  Ex...'''
date = "2015-09-21T01:13:00Z"
lastmod = "2016-02-20T01:25:00Z"
weight = 45995
keywords = [ "mate", "sip", "megaco" ]
aliases = [ "/questions/45995" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Mate Gop's not collected in same Gog.](/questions/45995/wireshark-mate-gops-not-collected-in-same-gog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45995-score" class="post-score" title="current number of votes">0</div><span id="post-45995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I'm trying to use Mate to collect SIP and Megaco messages. This has been tried by a number of times as it exist a number of questions on the web, but I have not get any answer.</p><p>I have the following Mate configuration:</p><pre><code>Pdu sip_msg Proto sip Transport ip {
        Extract sip_callid From sip.Call-ID;
        Extract sip_method From sip.Method;
        Extract sip_cseq_method From sip.CSeq.method;
        Extract sip_media_port From sdp.media.port;
    };

Gop sip_dialogue On sip_msg Match (sip_callid) {
    Start(sip_method=&quot;INVITE&quot;);
    Stop(sip_cseq_method=&quot;BYE&quot;);
    Extra (sip_media_port);
};

Pdu megaco_msg Proto megaco Transport sctp {
    Extract megaco_media_port From sdp.media.port;
    Extract megaco_transid From megaco.transid; 
    Extract megaco_transaction From megaco.transaction;
};

Gop megaco_dialogue On megaco_msg Match (megaco_transid) {
    Start(megaco_transaction=&quot;Request&quot;);
    Stop(megaco_transaction=&quot;Reply&quot;);
    Extra (megaco_media_port);
};

Gog complete_call {
    Member sip_dialogue (sip_media_port);
    Member megaco_dialogue (megaco_media_port);
};</code></pre><p>As you can see is the media port used to correlate SIP and Megaco, but it fails.</p><p>For one call is the following media port used (in the Gog Attributes):</p><pre><code>Megaco SIP
62888  6288
24560  24560
47126
54928  54928
15006</code></pre><p>Megaco has two more ports and I think, but not sure, this is the reason why they are are not correlated.</p><p>Does someone knows how to get this to work? Can the "Loose" statement be used? I do not know how to use it in the Mate configuration.</p><p>Thanks in advance Andreas</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-megaco" rel="tag" title="see questions tagged &#39;megaco&#39;">megaco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/e05bc0ed98b4b16bfe440ed5f9a8564c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreas%20J&#39;s gravatar image" /><p><span>Andreas J</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreas J has no accepted answers">0%</span></p></div></div><div id="comments-container-45995" class="comments-container"><span id="46060"></span><div id="comment-46060" class="comment"><div id="post-46060-score" class="comment-score"></div><div class="comment-text"><p>I'm not quite sure what you're saying. A single <code>complete_call</code> GoG should have only one mport (which is the same in the <code>megaco_dialog</code> and the <code>sip_dialog</code> compontents of that GoG), right?</p><p>I'm not sure what all these other ports are.</p></div><div id="comment-46060-info" class="comment-info"><span class="comment-age">(22 Sep '15, 10:28)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="50365"></span><div id="comment-50365" class="comment"><div id="post-50365-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Andreas J</span>, if still interesting, I'll try to clarify what <span></span><span>@JeffMorris</span> wrote: the name of the attribute used as the key to aggregate matching Gops into a Gog must be <em>literally the same</em> for all Member Gops. The statement</p><pre><code>Gog gog_name {
    Member dlg_1 ( port_1 );
    Member dlg_2 ( port_2 );
}</code></pre><p>does <em>not</em> mean, in MATE syntax, that values of attribute <code>port_1</code> of Gop <code>dlg_1</code> would be <em>treated the same way</em> like the values of attribute <code>port_2</code> of Gop <code>dlg_2</code>; it just means that values of <code>port_1</code> should be <em>looked for</em> in Gogs named <code>dlg_1</code>, and values of <code>port_2</code> should be <em>looked for</em> in Gogs named <code>dlg_2</code>.</p><p>So unless <code>port_1</code> is literally the same string like <code>port_2</code>, all <code>dlg_1</code> with the same <code>port_1</code> values would be grouped together, and all <code>dlg_2</code> with the same <code>port_2</code> values would also be grouped together, but even for identical <em>values</em> of <code>port_1</code> and <code>port_2</code>, these groups of Gops would remain separate from each other although they would have the same Gog <em>name</em> <code>gog_name</code>.</p><p>So all the way up from Pdu through Gop to Gog, you must use the same identifier, like <code>media_port</code>:</p><pre><code>Pdu sip_msg Proto sip Transport ip {
    Extract sip_callid From sip.Call-ID;
    Extract sip_method From sip.Method;
    Extract sip_cseq_method From sip.CSeq.method;
    Extract media_port From sdp.media.port;
};

Gop sip_dialogue On sip_msg Match (sip_callid) {
    Start(sip_method=&quot;INVITE&quot;);
    Stop(sip_cseq_method=&quot;BYE&quot;);
    Extra (media_port);
};

Pdu megaco_msg Proto megaco Transport sctp {
    Extract media_port From sdp.media.port;
    Extract megaco_transid From megaco.transid; 
    Extract megaco_transaction From megaco.transaction;
};

Gop megaco_dialogue On megaco_msg Match (megaco_transid) {
    Start(megaco_transaction=&quot;Request&quot;);
    Stop(megaco_transaction=&quot;Reply&quot;);
    Extra (media_port);
};

Gog complete_call {
    Member sip_dialogue (media_port);
    Member megaco_dialogue (media_port);
};</code></pre><p>A loose match has a different meaning and is not applicable here.</p></div><div id="comment-50365-info" class="comment-info"><span class="comment-age">(20 Feb '16, 01:25)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50366"></span><div id="comment-50366" class="comment"><div id="post-50366-score" class="comment-score"></div><div class="comment-text"><p>But that's still not all. I would need a sample capture to be 100 % sure, but if you collect more values of <code>media_port</code> per <code>sip_dialogue</code> or <code>megaco_dialogue</code> (as you definitely do at least because you do not distinguish between local SDP and remote SDP, so you do have two <code>media_port</code> per dialog, leaving aside that there may be multiple media streams per SDP and multiple SDPs per party of a dialog), the Gog may still not be aggregated properly. So you would need to identify the proper one of the two SDPs available in each of the protocols and extract the media_port only from it, not from the other one.</p><p>Next, I somehow cannot imagine a scenario where the SIP and MEGACO would be captured on the same machine and would both <em>send</em> the same SDP; I can only imagine that you receive a remote SDP in SIP and forward it as local one in Megaco or vice versa. If this is the case, you may have several remote SDPs with the same media port but different media IP address, so you'd need to add the media IP address as an attribute in order to avoid mixing several dialogs together into a single Gog.</p></div><div id="comment-50366-info" class="comment-info"><span class="comment-age">(20 Feb '16, 01:25)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-45995" class="comment-tools"></div><div class="clear"></div><div id="comment-45995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

