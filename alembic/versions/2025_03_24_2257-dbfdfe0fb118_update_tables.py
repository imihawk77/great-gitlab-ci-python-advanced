"""update tables

Revision ID: dbfdfe0fb118
Revises: faea70d523c4
Create Date: 2025-03-24 22:57:31.890345

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "dbfdfe0fb118"
down_revision: Union[str, None] = "faea70d523c4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
