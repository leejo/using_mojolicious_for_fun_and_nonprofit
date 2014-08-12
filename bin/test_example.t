#!perl

use strict;
use warnings;

use Test::Most;
use Test::Mojo;

my $t = Test::Mojo->new( "GivenGain" );

foreach my $url (
    [ '/influence/', \&_ordered_by_influence_points ],
) {
    my $link  = $url->[0];
    my $order = $url->[1];

    $t->get_ok("/activists/projects$link")
        ->status_is(200)
        ->content_like(qr/Explore Activists by Project/i);

    $t->tx->res->content =~ /Explore Activists by Project/i
        && $order->( $t );
}

done_testing();

sub _ordered_by_influence_points {

    my ( $t ) = @_;

    my @influence_points =
        map { $_ =~ s/\D//g; $_ }
        $t->tx->res->content->build_body =~ /\((.+) iPV\)/g;

    cmp_deeply(
        \@influence_points,
        [ sort { $b <=> $a } @influence_points ],
        'links ordered by influence points descending'
    );
}
