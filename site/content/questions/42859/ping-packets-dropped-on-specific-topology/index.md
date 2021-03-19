+++
type = "question"
title = "Ping packets dropped on specific topology"
description = '''Hi, I&#x27;m using wireshark to verify traffic on a mininet topology. It works for small topologies, but fails on larger ones. The topology I am trying it on is attached. Specifically, I am trying to ping h8 (attached to s37) from h1. Any pointers on how to fix this will be appreciated. &quot;&quot;&quot;  Refer to doc...'''
date = "2015-06-03T13:58:00Z"
lastmod = "2015-06-03T14:21:00Z"
weight = 42859
keywords = [ "ping" ]
aliases = [ "/questions/42859" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ping packets dropped on specific topology](/questions/42859/ping-packets-dropped-on-specific-topology)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42859-score" class="post-score" title="current number of votes">0</div><span id="post-42859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using wireshark to verify traffic on a mininet topology. It works for small topologies, but fails on larger ones. The topology I am trying it on is attached. Specifically, I am trying to ping h8 (attached to s37) from h1. Any pointers on how to fix this will be appreciated.</p><pre><code>&quot;&quot;&quot;</code></pre><p>Refer to docs in directory for pictorial representation of topology. """</p><p>from mininet.topo import Topo</p><p>class ThirtyNineBus( Topo ): '''The canonical 39-Bus topology'''</p><pre><code>def __init__( self ):

    # Initialize topology
    Topo.__init__( self )

    # Add switches
    s1 = self.addSwitch( &#39;s1&#39; )
    s2 = self.addSwitch( &#39;s2&#39; )
    s3 = self.addSwitch( &#39;s3&#39; )
    s4 = self.addSwitch( &#39;s4&#39; )
    s5 = self.addSwitch( &#39;s5&#39; )
    s6 = self.addSwitch( &#39;s6&#39; )
    s7 = self.addSwitch( &#39;s7&#39; )
    s8 = self.addSwitch( &#39;s8&#39; )
    s9 = self.addSwitch( &#39;s9&#39; )
    s10 = self.addSwitch( &#39;s10&#39; )
    s11 = self.addSwitch( &#39;s11&#39; )
    s12 = self.addSwitch( &#39;s12&#39; )
    s13 = self.addSwitch( &#39;s13&#39; )
    s14 = self.addSwitch( &#39;s14&#39; )
    s15 = self.addSwitch( &#39;s15&#39; )
    s16 = self.addSwitch( &#39;s16&#39; )
    s17 = self.addSwitch( &#39;s17&#39; )
    s18 = self.addSwitch( &#39;s18&#39; )
    s19 = self.addSwitch( &#39;s19&#39; )
    s20 = self.addSwitch( &#39;s20&#39; )
    s21 = self.addSwitch( &#39;s21&#39; )
    s22 = self.addSwitch( &#39;s22&#39; )
    s23 = self.addSwitch( &#39;s23&#39; )
    s24 = self.addSwitch( &#39;s24&#39; )
    s25 = self.addSwitch( &#39;s25&#39; )
    s26 = self.addSwitch( &#39;s26&#39; )
    s27 = self.addSwitch( &#39;s27&#39; )
    s28 = self.addSwitch( &#39;s28&#39; )
    s29 = self.addSwitch( &#39;s29&#39; )
    s30 = self.addSwitch( &#39;s30&#39; )
    s31 = self.addSwitch( &#39;s31&#39; )
    s32 = self.addSwitch( &#39;s32&#39; )
    s33 = self.addSwitch( &#39;s33&#39; )
    s34 = self.addSwitch( &#39;s34&#39; )
    s35 = self.addSwitch( &#39;s35&#39; )
    s36 = self.addSwitch( &#39;s36&#39; )
    s37 = self.addSwitch( &#39;s37&#39; )
    s38 = self.addSwitch( &#39;s38&#39; )
    s39 = self.addSwitch( &#39;s39&#39; )

    # add hosts
    # note: ignoring arrows
    h1 = self.addSwitch( &#39;h1&#39; )
    h2 = self.addSwitch( &#39;h2&#39; )
    h3 = self.addSwitch( &#39;h3&#39; )
    h4 = self.addSwitch( &#39;h4&#39; )
    h5 = self.addSwitch( &#39;h5&#39; )
    h6 = self.addSwitch( &#39;h6&#39; )
    h7 = self.addSwitch( &#39;h7&#39; )
    h8 = self.addSwitch( &#39;h8&#39; )
    h9 = self.addSwitch( &#39;h9&#39; )
    h10 = self.addSwitch( &#39;h10&#39; )

    # Add links
    # note: links are bidirectional 
    # =&gt; no need to add the same link from both sides
    # 1. switch-switch links
    self.addLink( s1, s2   )
    self.addLink( s1, s39  )
    self.addLink( s2, s30  )
    self.addLink( s2, s25  )
    self.addLink( s2, s3   )
    self.addLink( s3, s4   )
    self.addLink( s3, s18  )
    self.addLink( s4, s5   )
    self.addLink( s4, s14  )
    self.addLink( s5, s6   )
    self.addLink( s5, s8   )
    self.addLink( s6, s7   )
    self.addLink( s6, s11  )
    self.addLink( s6, s31  )
    self.addLink( s7, s8   )
    self.addLink( s8, s9   )
    self.addLink( s9, s39  )
    self.addLink( s10, s11 )
    self.addLink( s10, s13 )
    self.addLink( s10, s32 )
    self.addLink( s11, s12 )
    self.addLink( s12, s13 )
    self.addLink( s13, s14 )
    self.addLink( s14, s15 )
    self.addLink( s15, s16 )
    self.addLink( s16, s17 )
    self.addLink( s16, s19 )
    self.addLink( s16, s21 )
    self.addLink( s16, s24 )
    self.addLink( s17, s18 )
    self.addLink( s17, s27 )
    #self.addLink( s18, &lt;none&gt; )
    self.addLink( s19, s20 )
    self.addLink( s19, s33 )
    self.addLink( s20, s34 )
    self.addLink( s21, s22 )
    self.addLink( s22, s23 )
    self.addLink( s22, s35 )
    self.addLink( s23, s24 )
    self.addLink( s23, s36 )
    #self.addLink( s24, &lt;none&gt; )
    self.addLink( s25, s37 )
    self.addLink( s26, s27 )
    self.addLink( s26, s28 )
    self.addLink( s26, s29 )
    #self.addLink( s27, &lt;none&gt; )
    self.addLink( s28, s29 )
    self.addLink( s29, s38 )
    #self.addLink( s30, &lt;none&gt; )
    #self.addLink( s31, &lt;none&gt; )
    #self.addLink( s32, &lt;none&gt; )
    #self.addLink( s33, &lt;none&gt; )
    #self.addLink( s34, &lt;none&gt; )
    #self.addLink( s35, &lt;none&gt; )
    #self.addLink( s36, &lt;none&gt; )
    #self.addLink( s37, &lt;none&gt; )
    #self.addLink( s38, &lt;none&gt; )
    #self.addLink( s39, &lt;none&gt; )

    # 2. switch-host links
    self.addLink( s30, h1  )
    self.addLink( s31, h2  )
    self.addLink( s32, h3  )
    self.addLink( s33, h4  )
    self.addLink( s34, h5  )
    self.addLink( s35, h6  )
    self.addLink( s36, h7  )
    self.addLink( s37, h8  )
    self.addLink( s38, h9  )
    self.addLink( s39, h10 )</code></pre><p>topos = { 'ThirtyNineBus': ( lambda: ThirtyNineBus() ) }</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/039152feebd25423ee3733437ddf2566?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taki%20Chowdhury&#39;s gravatar image" /><p><span>Taki Chowdhury</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taki Chowdhury has no accepted answers">0%</span></p></div></div><div id="comments-container-42859" class="comments-container"><span id="42860"></span><div id="comment-42860" class="comment"><div id="post-42860-score" class="comment-score"></div><div class="comment-text"><p>Never mind! The error was in my code-it should be h1 = self.addHost('h1') and not addSwitch()!</p></div><div id="comment-42860-info" class="comment-info"><span class="comment-age">(03 Jun '15, 14:21)</span> <span class="comment-user userinfo">Taki Chowdhury</span></div></div></div><div id="comment-tools-42859" class="comment-tools"></div><div class="clear"></div><div id="comment-42859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

