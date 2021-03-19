+++
type = "question"
title = "IP dissector does not recognize my protocol"
description = '''I&#x27;m developing a dissector/protocol as a plugin above Network layer so that The IP dissector will dissect all the IP headers and will look at the &quot;protocol&quot; field to pass the payload to my protocol. let&#x27;s say the protocol number is &quot; 254 &quot;. It runs over IP. What are all the steps needed to do , so t...'''
date = "2015-06-05T03:23:00Z"
lastmod = "2015-06-07T08:43:00Z"
weight = 42912
keywords = [ "dissector", "protocol", "wireshark" ]
aliases = [ "/questions/42912" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IP dissector does not recognize my protocol](/questions/42912/ip-dissector-does-not-recognize-my-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42912-score" class="post-score" title="current number of votes">0</div><span id="post-42912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing a dissector/protocol as a plugin above Network layer so that The IP dissector will dissect all the IP headers and will look at the "protocol" field to pass the payload to my protocol. let's say the protocol number is " 254 ".<br />
It runs over IP.<br />
What are all the steps needed to do , so that the IP dissector recognize the protocol and it will pass the payload to my protocol ?</p><p>This is not a heuristic dissector.</p><p>EDIT : my packet-temp.c file contains :</p><pre><code>#include &quot;config.h&quot;

#include &lt; epan/packet.h&gt;

#define IP_PROTO_TEMP 254
static int proto_temp = -1;

static void dissect_temp(tvbuff_t *tvb, packet_info *pinfo, proto_tree     *tree)
{
      col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;TEMP&quot;);
      /* Clear out stuff in the info column */
      col_clear(pinfo-&gt;cinfo, COL_INFO);
 }

 void proto_register_temp(void)
 {
       proto_temp = proto_register_protocol (
                 &quot;TEMP Protocol&quot;, /* name       */
                 &quot;TEMP&quot;,      /* short name */
                 &quot;temp&quot;       /* abbrev     */
                 );
  }

  void proto_reg_handoff_temp(void)
 {
      static dissector_handle_t temp_handle;

      temp_handle = create_dissector_handle(dissect_temp, proto_temp);
      dissector_add_uint(&quot;ip.port&quot;, IP_PROTO_TEMP , temp_handle);
 }</code></pre><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '15, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/ea74f093a0efe137c7c114da864fa5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sammee%20Sharma&#39;s gravatar image" /><p><span>Sammee Sharma</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sammee Sharma has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '15, 07:49</strong> </span></p></div></div><div id="comments-container-42912" class="comments-container"></div><div id="comment-tools-42912" class="comment-tools"></div><div class="clear"></div><div id="comment-42912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42916"></span>

<div id="answer-container-42916" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42916-score" class="post-score" title="current number of votes">2</div><span id="post-42916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sammee Sharma has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, This is what packet-tcp.c does:</p><pre><code>dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_TCP, tcp_handle);</code></pre><p>replace IP_PROTO_TCP with your number and the handle with your protocol handle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '15, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '15, 04:13</strong> </span></p></div></div><div id="comments-container-42916" class="comments-container"><span id="42918"></span><div id="comment-42918" class="comment"><div id="post-42918-score" class="comment-score"></div><div class="comment-text"><p>You should register your protocol with IANA.</p></div><div id="comment-42918-info" class="comment-info"><span class="comment-age">(05 Jun '15, 04:26)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="42938"></span><div id="comment-42938" class="comment"><div id="post-42938-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply <span>@Anders</span> . I replaced IP_PROTO_TCP with my protocol number(254) and tcp_handle with my protocol handle. But still I could not see my protocol number in the ipproto.c file or ip.proto table. Am i missing something?</p></div><div id="comment-42938-info" class="comment-info"><span class="comment-age">(06 Jun '15, 05:07)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div><span id="42939"></span><div id="comment-42939" class="comment"><div id="post-42939-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you mean. Isn't your dissector being called? If you check the menu item internal integer dissector tables in.protocol, is your protocol registered there? If not you are not registering it properly.</p></div><div id="comment-42939-info" class="comment-info"><span class="comment-age">(06 Jun '15, 07:24)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="42940"></span><div id="comment-42940" class="comment"><div id="post-42940-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Anders</span> sir, I've checked (Internals -&gt;Dissector table -&gt; Integer tables -&gt; ip.proto ) in the wireshark but it's not there. I've attached the packet-temp.c code. please have a look at it . waiting for your suggestion.Thanks.</p></div><div id="comment-42940-info" class="comment-info"><span class="comment-age">(06 Jun '15, 07:55)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div><span id="42941"></span><div id="comment-42941" class="comment not_top_scorer"><div id="post-42941-score" class="comment-score"></div><div class="comment-text"><p>Did you also replace "ip.port" by "ip.proto", as the table to register too?</p></div><div id="comment-42941-info" class="comment-info"><span class="comment-age">(06 Jun '15, 09:21)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42942"></span><div id="comment-42942" class="comment not_top_scorer"><div id="post-42942-score" class="comment-score"></div><div class="comment-text"><p>with this modification , i see that protocol number(254) in (wireshark -&gt; Internals -&gt;Dissector table -&gt; Integer tables -&gt; ip.proto ) but it is not there in ipproto.c file. should it be not there? <span>@jaap</span></p></div><div id="comment-42942-info" class="comment-info"><span class="comment-age">(07 Jun '15, 05:08)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div><span id="42945"></span><div id="comment-42945" class="comment"><div id="post-42945-score" class="comment-score">1</div><div class="comment-text"><p>No. The <code>dissector_add_uint</code> call causes a run-time modification, not a compile time one. This allows additions of new protocols without having to modify ipproto.c</p></div><div id="comment-42945-info" class="comment-info"><span class="comment-age">(07 Jun '15, 08:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42916" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-42916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

