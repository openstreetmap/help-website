+++
type = "question"
title = "Plugin works in 1.10.07 but not in 1.11.03 (normal ?)"
description = '''Hello, After a long way :D I have written my RTP Extensions. So first I would like to say thanks, because I get help from that forum. I have written my Plugin and have compiled it with MS VS 2012 with the source from the stable 1.10.07. Now I have a 32 bit plugin.dll. That is very nice and Works wit...'''
date = "2014-04-28T06:20:00Z"
lastmod = "2014-04-28T11:13:00Z"
weight = 32250
keywords = [ "versions", "plugins", "plugin" ]
aliases = [ "/questions/32250" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Plugin works in 1.10.07 but not in 1.11.03 (normal ?)](/questions/32250/plugin-works-in-11007-but-not-in-11103-normal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32250-score" class="post-score" title="current number of votes">0</div><span id="post-32250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>After a long way :D I have written my RTP Extensions. So first I would like to say thanks, because I get help from that forum.</p><p>I have written my Plugin and have compiled it with MS VS 2012 with the source from the stable 1.10.07. Now I have a 32 bit plugin.dll. That is very nice and Works with the stable Version 1.10.07 very good.</p><p>Now I would like to change to Version 1.11.03. So I have Install that Version, but with my Plugin Wireshark don't start. I have then download the source code and build my Plugin with the 1.11.03 and with that new dll Wireshark start with the Version 1.11.03.</p><p>Now my Question: Is it possible to make a plugin what works in 1.10.07 and 1.11.03 without recompile?</p><p>My Plugin looks like: I Post the code but i dont think it is important for my Question</p><pre><code>#include &quot;config.h&quot;
#include glib.h
#include epan/packet.h
#include &quot;packet-rtpExtensions.h&quot;

void proto_register_rsExtensions(void);
void proto_reg_handoff_rsExtensions(void);

static int rtpext = 0x0001;  
static int rtpproto= 0x80;

static void
proto_register_rsExtensions(void)
{   ...    }

static void
extdissectxtensions(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{   .... }
static void
dissectxtensions(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{   .... }

void
proto_reg_handoff_rsExtensions(void)
{
 dissector_handle_t dis1; 
 dissector_handle_t dis2;

rdeo = create_dissector_handle( extdissectxtensions, foo); 
dissector_add_uint(&quot;rtp.hdr_ext&quot;, rtpext , rdeo );

rEx = create_dissector_handle( dissectxtensions, foo); 
dissector_add_uint(&quot;rtp.pt&quot;, rtpproto, rEx );

}</code></pre><p>Have a nice day</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-versions" rel="tag" title="see questions tagged &#39;versions&#39;">versions</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/3378e4af34b02834b98e8a896efe303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alias_alias&#39;s gravatar image" /><p><span>Alias_alias</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alias_alias has no accepted answers">0%</span></p></div></div><div id="comments-container-32250" class="comments-container"></div><div id="comment-tools-32250" class="comment-tools"></div><div class="clear"></div><div id="comment-32250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32252"></span>

<div id="answer-container-32252" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32252-score" class="post-score" title="current number of votes">2</div><span id="post-32252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alias_alias has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>too many internal APIs have changed between 1.10 branch and the 1.12 development branch to ensure that you have a plugin compatible between major versions.</p><p>That's the drawback with plugins: you need to provide one library per major (stable) version. You can use compilation flags to have a single source code, but the recompilation is unavoidable unfortunately.</p><p>For your information, once a major version is frozen (1.10.0 or 1.12.0), we try to keep the APIs stable between minor versions (1.10.1, 1.10.2, ...) so as to ensure compatibility.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-32252" class="comments-container"><span id="32254"></span><div id="comment-32254" class="comment"><div id="post-32254-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks. That is not perfekt but Ok.</p><p>How can i add compilation flags ? I never have make this did you have an example ?</p></div><div id="comment-32254-info" class="comment-info"><span class="comment-age">(28 Apr '14, 07:56)</span> <span class="comment-user userinfo">Alias_alias</span></div></div><span id="32267"></span><div id="comment-32267" class="comment"><div id="post-32267-score" class="comment-score"></div><div class="comment-text"><p>You can use the VERSION_MAJOR, VERSION_MINOR and VERSION_MICRO defines to identify the Wireshark source code used to build your plugin.</p></div><div id="comment-32267-info" class="comment-info"><span class="comment-age">(28 Apr '14, 11:13)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-32252" class="comment-tools"></div><div class="clear"></div><div id="comment-32252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

