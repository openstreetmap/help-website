+++
type = "question"
title = "Structure for dissector plugin"
description = '''I have a custom header as {version[2 bits], control[8 bits], high[6 bits], low[11 bits], index[5 bits]} I am trying to create the data structure for my dissector plugin and I am having trouble with it. Currently my structure looks like this:  { &amp;amp;hf_packet_skip1,  { &quot;PACKET SKIP1&quot;, &quot;packet.skip1&quot;...'''
date = "2015-09-25T00:52:00Z"
lastmod = "2015-09-25T06:52:00Z"
weight = 46137
keywords = [ "packet", "dissector", "tshark", "plugin", "wireshark" ]
aliases = [ "/questions/46137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Structure for dissector plugin](/questions/46137/structure-for-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46137-score" class="post-score" title="current number of votes">0</div><span id="post-46137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a custom header as {version[2 bits], control[8 bits], high[6 bits], low[11 bits], index[5 bits]}</p><p>I am trying to create the data structure for my dissector plugin and I am having trouble with it.</p><p>Currently my structure looks like this:</p><pre><code>      { &amp;hf_packet_skip1,
          { &quot;PACKET SKIP1&quot;, &quot;packet.skip1&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      },
      { &amp;hf_packet_version,
          { &quot;PACKET VERSION&quot;, &quot;packet.skip1.version&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      },    
      { &amp;hf_packet_control,
          { &quot;PACKET CONTROL&quot;, &quot;packet.skip1.control&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      },
      { &amp;hf_packet_high,
          { &quot;PACKET HIGH&quot;, &quot;packet.skip1.high&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      },
      { &amp;hf_packet_skip2,
          { &quot;PACKET SKIP2&quot;, &quot;packet.skip2&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      }
      { &amp;hf_packet_low,
          { &quot;PACKET LOW&quot;, &quot;packet.skip2.low&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      }
      { &amp;hf_packet_index,
          { &quot;PACKET INDEX&quot;, &quot;packet.skip2.index&quot;,
          FT_UINT16, BASE_DEC,
          NULL, 0x0,
          NULL, HFILL }
      }</code></pre><p>Please help me get the correct structure.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '15, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/5c6557bd7c8696a17e1c44bae9cd4217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samprit&#39;s gravatar image" /><p><span>samprit</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samprit has no accepted answers">0%</span></p></div></div><div id="comments-container-46137" class="comments-container"></div><div id="comment-tools-46137" class="comment-tools"></div><div class="clear"></div><div id="comment-46137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46148"></span>

<div id="answer-container-46148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46148-score" class="post-score" title="current number of votes">0</div><span id="post-46148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Change the '0x0' fields to applicable values for a bitmask to get desired field values.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46148" class="comments-container"><span id="46162"></span><div id="comment-46162" class="comment"><div id="post-46162-score" class="comment-score"></div><div class="comment-text"><p>I am currently stuck. Can you please show an example as to what value should I change it to.</p></div><div id="comment-46162-info" class="comment-info"><span class="comment-age">(25 Sep '15, 05:46)</span> <span class="comment-user userinfo">samprit</span></div></div><span id="46167"></span><div id="comment-46167" class="comment"><div id="post-46167-score" class="comment-score"></div><div class="comment-text"><p>It always helps to look at other dissectors to see how they addressed the issue at hand. Of course you'll need to understand that dissectors protocol as well, but who doesn't know about IPv4? So have a look at packet-ip.c and see how the structures are setup for some of their fields covering only a few bits of an octet. Oh, and for more details checkout doc/README</p></div><div id="comment-46167-info" class="comment-info"><span class="comment-age">(25 Sep '15, 06:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-46148" class="comment-tools"></div><div class="clear"></div><div id="comment-46148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

