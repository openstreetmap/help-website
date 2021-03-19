+++
type = "question"
title = "Lua Examples to parse custom headers inside GRE"
description = '''Hi, I am writing a dissector for parsing new data structure within the GRE. Ethernet+IPHEADER(OUTER)+GRE+Customdatastruct+Original( IP+TCP PACKET) as part of payload. I am not sure what debugs can be turned on with Lua. My dissector is not working, it cannot parse the values inside the GRE packet. C...'''
date = "2011-01-18T20:57:00Z"
lastmod = "2012-04-30T16:03:00Z"
weight = 1803
keywords = [ "lua", "processing", "gre", "packet" ]
aliases = [ "/questions/1803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua Examples to parse custom headers inside GRE](/questions/1803/lua-examples-to-parse-custom-headers-inside-gre)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1803-score" class="post-score" title="current number of votes">0</div><span id="post-1803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am writing a dissector for parsing new data structure within the GRE. Ethernet+IPHEADER(OUTER)+GRE+Customdatastruct+Original( IP+TCP PACKET) as part of payload.</p><p>I am not sure what debugs can be turned on with Lua. My dissector is not working, it cannot parse the values inside the GRE packet. Can someone throw some light on this ?</p><p>I successed upto the point it shows GRE value as 47, flags and version as 0000, the protocol field is also displayed, beyond that it shows as DATA. It should have parsed all the fields, and also should have shown me the inner headers as well.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-processing" rel="tag" title="see questions tagged &#39;processing&#39;">processing</span> <span class="post-tag tag-link-gre" rel="tag" title="see questions tagged &#39;gre&#39;">gre</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '11, 20:57</strong></p><img src="https://secure.gravatar.com/avatar/f176a81caa3098bf81d6683fc05a6cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="balaji&#39;s gravatar image" /><p><span>balaji</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="balaji has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '12, 20:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1803" class="comments-container"><span id="1804"></span><div id="comment-1804" class="comment"><div id="post-1804-score" class="comment-score"></div><div class="comment-text"><p>Balaji Writes :</p><p>Syntax wise the code is correct, but I still cannot parse the fields below the flags and version of GRE header. Do you have a sample code as an example to parse custom headers inside GRE ? Do you have a sample code for WCCP Redirection inside GRE or IPSEC tunnels written in LUA ?</p></div><div id="comment-1804-info" class="comment-info"><span class="comment-age">(18 Jan '11, 21:07)</span> <span class="comment-user userinfo">balaji</span></div></div><span id="10540"></span><div id="comment-10540" class="comment"><div id="post-10540-score" class="comment-score">1</div><div class="comment-text"><p>would you mind to post your lua code?</p></div><div id="comment-10540-info" class="comment-info"><span class="comment-age">(30 Apr '12, 16:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-1803" class="comment-tools"></div><div class="clear"></div><div id="comment-1803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

